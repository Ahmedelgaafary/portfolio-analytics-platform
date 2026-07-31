"""
                        covariance.py

                        Part of Portfolio Analytics Platform.
                        

Covariance calculations.
"""

from __future__ import annotations

import logging

import pandas as pd

logger = logging.getLogger(__name__)


class CovarianceCalculator:
    """
    Calculate covariance matrices.
    """

    def covariance_matrix(
        self,
        returns: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info(
            "Calculating covariance matrix."
        )

        return returns.cov()

    def annualized_covariance(
        self,
        returns: pd.DataFrame,
        trading_days: int = 252,
    ) -> pd.DataFrame:

        logger.info(
            "Calculating annual covariance."
        )

        return returns.cov() * trading_days