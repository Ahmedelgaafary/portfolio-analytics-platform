"""
                        correlation.py

                        Part of Portfolio Analytics Platform.
                        
Correlation calculations.
"""

from __future__ import annotations

import logging

import pandas as pd

logger = logging.getLogger(__name__)


class CorrelationCalculator:
    """
    Calculate correlation matrices.
    """

    def correlation_matrix(
        self,
        returns: pd.DataFrame,
    ) -> pd.DataFrame:

        logger.info(
            "Calculating correlation matrix."
        )

        return returns.corr()