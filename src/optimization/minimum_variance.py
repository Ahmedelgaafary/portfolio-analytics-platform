"""
                        minimum_variance.py

                        Part of Portfolio Analytics Platform.
Minimum Variance optimizer.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize

from .constraints import Constraints
from .objective_functions import ObjectiveFunctions


class MinimumVarianceOptimizer:

    def optimize(
        self,
        covariance,
    ):

        n = covariance.shape[0]

        initial = np.ones(n) / n

        result = minimize(
            ObjectiveFunctions.portfolio_variance,
            initial,
            args=(covariance,),
            method="SLSQP",
            bounds=Constraints.bounds(n),
            constraints=Constraints.weight_sum(),
        )

        if not result.success:
            raise RuntimeError(result.message)

        return result.x