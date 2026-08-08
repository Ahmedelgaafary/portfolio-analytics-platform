""" downloader.py 
Part of Portfolio Analytics Platform.

Market data downloader.

Provides classes for downloading historical financial market data.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict

import pandas as pd
import yfinance as yf
from src.data_processing.cache import CacheManager

logger = logging.getLogger(__name__)


class MarketDataDownloader:
    """
    Download historical financial market data.

    This class provides methods for downloading one or
    multiple assets from Yahoo Finance.
    """

    def __init__(
        self,
        cache_dir: Path | str = "data/cache",
        auto_adjust: bool = True,
    ):
        self.cache_dir = Path(cache_dir)
        self.auto_adjust = auto_adjust

        self.cache_dir.mkdir(
            parents=True,
            exist_ok=True,
        )
        self.cache = CacheManager(self.cache_dir)


    def validate_tickers(
        self,
        tickers: str | list[str],
    ) -> list[str]:
        """Validate and normalize ticker symbols."""
        if isinstance(tickers, str):
            tickers = [tickers]

        if not isinstance(tickers, list):
            raise TypeError(
                "Tickers must be a string or a list of strings."
            )

        cleaned = []

        for ticker in tickers:

            if not isinstance(ticker, str):
                raise TypeError(
                    "Each ticker must be a string."
                )

            ticker = ticker.strip().upper()

            if ticker:
                cleaned.append(ticker)

        if not cleaned:
            raise ValueError(
                "No valid ticker symbols provided."
            )

        return cleaned

    def download(
        self,
        ticker: str,
        start: str,
        end: str,
        interval: str = "1d",
        use_cache: bool = False,
    ) -> pd.DataFrame:
        """
        Download historical price data for a single asset.
        """
        ticker = self.validate_tickers(ticker)[0]

        logger.info("Downloading %s", ticker)
        # ----------------------------
        # Load from cache if available
        # ----------------------------
        if use_cache and self.cache.exists(ticker):

            logger.info(
                "Loading %s from cache.",
                ticker,
            )

            return self.cache.load(ticker)
        try:
            df = yf.download(
                tickers=ticker,
                start=start,
                end=end,
                interval=interval,
                auto_adjust=self.auto_adjust,
                progress=False,
            )
            
            if df.empty:
                raise ValueError(
                    f"No data returned for ticker '{ticker}'."
                )

            df = df.sort_index()
        
            # ----------------------------
            # Save to cache
            # ----------------------------
            
            if use_cache:
                self.cache.save(
                    ticker=ticker,
                    data=df,
                )

            logger.info(
                "Successfully downloaded %s",
                ticker,
            )

            return df


        except Exception as exc:
            logger.exception(
                "Failed to download data for %s",
                ticker,
            )

            raise RuntimeError(
                f"Unable to download data for '{ticker}'."
            ) from exc
    def download_multiple(
        self,
        tickers: list[str],
        start: str,
        end: str,
        interval: str = "1d",
        use_cache: bool = False,
    ) -> pd.DataFrame:
        """
        Download historical closing prices for multiple assets.
        """

        tickers = self.validate_tickers(tickers)

        data = {}

        for ticker in tickers:

            try:

                prices = self.download(
                    ticker=ticker,
                    start=start,
                    end=end,
                    interval=interval,
                    use_cache=use_cache,
                )

                print(
                    ticker,
                    type(prices),
                    prices.shape,
                )
                close = prices["Close"]

                if isinstance(close, pd.DataFrame):
                    close = close.iloc[:, 0]

                data[ticker] = close

            except Exception as error:

                logger.warning(
                    "Skipping ticker %s: %s",
                    ticker,
                    error,
                )

        
        for ticker, values in data.items():

            print(
                ticker,
                type(values),
            )

        return pd.DataFrame(data)