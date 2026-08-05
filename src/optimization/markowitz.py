"""
                        markowitz.py

                        Part of Portfolio Analytics Platform.
                        

Markowitz Portfolio Optimizer.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from .maximum_sharpe import MaximumSharpeOptimizer


class MarkowitzOptimizer:
    """
    Classical Markowitz mean-variance optimizer.

    For Version 1 this optimizer returns the
    Maximum Sharpe portfolio.
    """

    def optimize(
        self,
        expected_returns: pd.Series,
        covariance: pd.DataFrame,
        risk_free_rate: float = 0.02,
    ) -> np.ndarray:

        optimizer = MaximumSharpeOptimizer()

        return optimizer.optimize(
            expected_returns=expected_returns,
            covariance=covariance,
            risk_free_rate=risk_free_rate,
        )