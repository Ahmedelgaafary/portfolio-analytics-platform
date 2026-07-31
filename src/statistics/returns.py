"""
                        returns.py

                        Part of Portfolio Analytics Platform.


Return calculations.
"""

from __future__ import annotations

import logging

import pandas as pd

import numpy as np

logger = logging.getLogger(__name__)


class ReturnsCalculator:
    """
    Calculate financial returns.
    """

    def simple_returns(
        self,
        prices: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Calculate simple percentage returns.
        """

        if prices.empty:
            raise ValueError("Price data is empty.")

        logger.info("Calculating simple returns.")

        return prices.pct_change().dropna()

    def log_returns(
        self,
        prices: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Calculate logarithmic returns.
        """

        if prices.empty:
            raise ValueError("Price data is empty.")

        logger.info("Calculating log returns.")

        return np.log(
            prices / prices.shift(1)
        ).dropna()

    def cumulative_returns(
        self,
        returns: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Calculate cumulative returns.
        """

        logger.info("Calculating cumulative returns.")

        return (1 + returns).cumprod() - 1