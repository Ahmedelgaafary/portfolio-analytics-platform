"""
                        minimum_variance.py

                        Part of Portfolio Analytics Platform.
Minimum Variance Portfolio Optimizer.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.optimize import minimize

from .constraints import Constraints
from .objective_functions import ObjectiveFunctions


class MinimumVarianceOptimizer:
    """
    Compute the global minimum variance portfolio.
    """

    def optimize(
        self,
        covariance: pd.DataFrame,
    ) -> np.ndarray:
        """
        Optimize portfolio weights by minimizing variance.

        Parameters
        ----------
        covariance : pd.DataFrame
            Annual covariance matrix.

        Returns
        -------
        np.ndarray
            Optimal portfolio weights.
        """

        n_assets = covariance.shape[0]

        initial_weights = np.ones(n_assets) / n_assets

        result = minimize(
            fun=ObjectiveFunctions.portfolio_variance,
            x0=initial_weights,
            args=(covariance,),
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