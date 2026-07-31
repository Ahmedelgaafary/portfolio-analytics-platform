"""
                        portfolio_statistics.py

                        Part of Portfolio Analytics Platform.
                        
Portfolio statistics.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class PortfolioStatistics:
    """
    Portfolio statistical calculations.
    """

    def expected_return(
        self,
        returns: pd.DataFrame,
        trading_days: int = 252,
    ) -> pd.Series:
        """
        Annualized expected return.
        """

        logger.info(
            "Calculating expected returns."
        )

        return returns.mean() * trading_days

    def portfolio_return(
        self,
        weights: np.ndarray,
        expected_returns: pd.Series,
    ) -> float:
        """
        Portfolio expected return.
        """

        return float(
            np.dot(
                weights,
                expected_returns,
            )
        )

    def portfolio_volatility(
        self,
        weights: np.ndarray,
        covariance: pd.DataFrame,
    ) -> float:
        """
        Portfolio volatility.
        """

        variance = (
            weights.T
            @ covariance.values
            @ weights
        )

        return float(np.sqrt(variance))

    def portfolio_variance(
        self,
        weights: np.ndarray,
        covariance: pd.DataFrame,
    ) -> float:
        """
        Portfolio variance.
        """

        return float(
            weights.T
            @ covariance.values
            @ weights
        )