"""
                        repository.py

                        Part of Portfolio Analytics Platform.

Repository layer for database operations.
"""

from __future__ import annotations

import logging

import pandas as pd

from src.database.connection import DatabaseManager
from src.database.models import (
    Backtest,
    Portfolio,
    Prediction,
)
from src.database.queries import (
    DELETE_PORTFOLIO,
    INSERT_BACKTEST,
    INSERT_PORTFOLIO,
    INSERT_PREDICTION,
    INSERT_PRICE,
    SELECT_BACKTESTS,
    SELECT_LATEST_PRICE,
    SELECT_PORTFOLIO,
    SELECT_PREDICTIONS,
    SELECT_PRICE_HISTORY,
)

logger = logging.getLogger(__name__)


class Repository:
    """
    Repository for all database operations.
    """

    def __init__(
        self,
        db: DatabaseManager,
    ) -> None:

        self.db = db

    # ======================================================
    # Prices
    # ======================================================

    def save_prices(
        self,
        ticker: str,
        prices: pd.DataFrame,
    ) -> None:
        """
        Save historical prices.
        """

        rows = []

        for date, row in prices.iterrows():

            rows.append(
                (
                    ticker,
                    str(date),
                    float(row["Open"]),
                    float(row["High"]),
                    float(row["Low"]),
                    float(row["Close"]),
                    int(row["Volume"]),
                )
            )

        self.db.executemany(
            INSERT_PRICE,
            rows,
        )

        logger.info(
            "Saved %s price rows for %s",
            len(rows),
            ticker,
        )

    def load_prices(
        self,
        ticker: str,
    ) -> pd.DataFrame:
        """
        Load historical prices.
        """

        rows = self.db.fetch_all(
            SELECT_PRICE_HISTORY,
            (ticker,),
        )

        if not rows:

            return pd.DataFrame()

        df = pd.DataFrame(
            rows,
            columns=[
                "Date",
                "Open",
                "High",
                "Low",
                "Close",
                "Volume",
            ],
        )

        df["Date"] = pd.to_datetime(df["Date"])

        df.set_index(
            "Date",
            inplace=True,
        )

        return df

    def latest_price(
        self,
        ticker: str,
    ):

        return self.db.fetch_one(
            SELECT_LATEST_PRICE,
            (ticker,),
        )

    # ======================================================
    # Predictions
    # ======================================================

    def save_prediction(
        self,
        prediction: Prediction,
    ) -> None:

        self.db.execute(
            INSERT_PREDICTION,
            (
                prediction.ticker,
                prediction.date,
                prediction.prediction,
                prediction.confidence,
                prediction.model,
            ),
        )

    def load_predictions(
        self,
        ticker: str,
    ):

        return self.db.fetch_all(
            SELECT_PREDICTIONS,
            (ticker,),
        )

    # ======================================================
    # Portfolio
    # ======================================================

    def save_portfolio(
        self,
        portfolio: list[Portfolio],
    ) -> None:
        """
        Save portfolio weights.
        """

        self.db.execute(
            DELETE_PORTFOLIO,
        )

        rows = []

        for asset in portfolio:

            rows.append(
                (
                    asset.ticker,
                    asset.weight,
                )
            )

        self.db.executemany(
            INSERT_PORTFOLIO,
            rows,
        )

    def load_portfolio(self):

        return self.db.fetch_all(
            SELECT_PORTFOLIO,
        )

    # ======================================================
    # Backtests
    # ======================================================

    def save_backtest(
        self,
        result: Backtest,
    ) -> None:

        self.db.execute(
            INSERT_BACKTEST,
            (
                result.strategy,
                result.annual_return,
                result.sharpe,
                result.max_drawdown,
            ),
        )

    def load_backtests(self):

        return self.db.fetch_all(
            SELECT_BACKTESTS,
        )