"""
                        maximum_sharpe.py

                        Part of Portfolio Analytics Platform.
                        
Maximum Sharpe Ratio Optimizer.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.optimize import minimize

from .constraints import Constraints
from .objective_functions import ObjectiveFunctions


class MaximumSharpeOptimizer:
    """
    Optimize portfolio weights by maximizing the Sharpe Ratio.
    """

    def optimize(
        self,
        expected_returns: pd.Series,
        covariance: pd.DataFrame,
        risk_free_rate: float = 0.02,
    ) -> np.ndarray:
        """
        Compute the maximum Sharpe ratio portfolio.

        Parameters
        ----------
        expected_returns : pd.Series
            Expected annual returns.

        covariance : pd.DataFrame
            Annual covariance matrix.

        risk_free_rate : float
            Annual risk-free rate.

        Returns
        -------
        np.ndarray
            Optimal portfolio weights.
        """

        n_assets = len(expected_returns)

        initial_weights = np.ones(n_assets) / n_assets

        result = minimize(
            fun=ObjectiveFunctions.negative_sharpe,
            x0=initial_weights,
            args=(
                expected_returns,
                covariance,
                risk_free_rate,
            ),
            method="SLSQP",
            bounds=Constraints.bounds(n_assets),
            constraints=Constraints.weight_sum(),
        )

        if not result.success:
            raise RuntimeError(
                f"Optimization failed: {result.message}"
            )

        weights = result.x

        weights /= weights.sum()

        return weights