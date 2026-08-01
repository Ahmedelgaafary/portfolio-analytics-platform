"""
                        markowitz.py

                        Part of Portfolio Analytics Platform.
                        
Markowitz optimizer.
"""

from __future__ import annotations

from .maximum_sharpe import MaximumSharpeOptimizer


class MarkowitzOptimizer:
    """
    Wrapper around the maximum Sharpe optimizer.
    """

    def optimize(
        self,
        expected_returns,
        covariance,
    ):

        optimizer = MaximumSharpeOptimizer()

        return optimizer.optimize(
            expected_returns,
            covariance,
        )