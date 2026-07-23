"""
                        cache.py

                        Part of Portfolio Analytics Platform.
                        
                        
Cache manager for market data.

Provides local storage of downloaded datasets to avoid
repeated downloads from external data providers.
"""

from __future__ import annotations

import logging
from os import path
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)


class CacheManager:
    """
    Manage cached market datasets.
    """

    def __init__(
        self,
        cache_dir: str | Path = "data/cache",
    ) -> None:

        self.cache_dir = Path(cache_dir)

        self.cache_dir.mkdir(
            parents=True,
            exist_ok=True,
        )
        
    def _cache_path(
    self,
    ticker: str,
) -> Path:
        """
        Return cache file path.
        """
        return self.cache_dir / f"{ticker}.parquet"
    
    def exists(
    self,
    ticker: str,
) -> bool:
    
        """
        Check whether cached data exists.
        """
        return self._cache_path(ticker).exists()
    def save(
        self,
        ticker: str,
        data: pd.DataFrame,
    ) -> None:
        """
        Save dataframe to cache.
        """

        path = self._cache_path(ticker)

        data.to_parquet(path)

        logger.info(
            "Saved cache for %s",
            ticker,
        )
    def load(
    self,
    ticker: str,
) -> pd.DataFrame:

        """
        Load dataframe from cache.
        """

        path = self._cache_path(ticker)

        if not path.exists():

            raise FileNotFoundError(
                f"No cache found for {ticker}"
            )

        logger.info(
            "Loading %s from cache",
            ticker,
        )

        return pd.read_parquet(path)
    
    def delete(
    self,
    ticker: str,
) -> None:

        path = self._cache_path(
            ticker
        )

        if path.exists():

            path.unlink()

            logger.info(
                "Deleted cache %s",
                ticker,
            )
            
    def clear(self) -> None:

        """
        Delete all cached datasets.
        """

        for file in self.cache_dir.glob(
            "*.parquet"
        ):
            file.unlink()

        logger.info(
            "Cache cleared."
        )