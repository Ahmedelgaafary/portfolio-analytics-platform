"""
                        performance.py

                        Part of Portfolio Analytics Platform.
                     
Performance analytics.
"""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd
logger = logging.getLogger(__name__)


class PerformanceAnalyzer:
    """
    Calculate portfolio performance metrics.
    """

    def annual_return(
        self,
        returns: pd.Series,
        trading_days: int = 252,
    ) -> float:
        """
        Calculate annualized compounded return.
        """

        if returns.empty:
            raise ValueError("Return series is empty.")

        logger.info("Calculating annual return.")

        return float(
            (1 + returns).prod()
            ** (trading_days / len(returns))
            - 1
        )

    def annual_volatility(
        self,
        returns: pd.Series,
        trading_days: int = 252,
    ) -> float:
        """
        Calculate annualized volatility.
        """

        if returns.empty:
            raise ValueError("Return series is empty.")

        logger.info("Calculating annual volatility.")

        return float(
            returns.std() * np.sqrt(trading_days)
        )

    def cumulative_return(
        self,
        returns: pd.Series,
    ) -> float:
        """
        Calculate cumulative return over the entire period.
        """

        if returns.empty:
            raise ValueError("Return series is empty.")

        logger.info("Calculating cumulative return.")

        cumulative = float((1 + returns).prod()) - 1.0

        return cumulative