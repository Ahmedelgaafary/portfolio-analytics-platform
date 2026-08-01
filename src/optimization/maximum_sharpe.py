"""
                        maximum_sharpe.py

                        Part of Portfolio Analytics Platform.
                        
Maximum Sharpe optimizer.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize

from .constraints import Constraints
from .objective_functions import ObjectiveFunctions


class MaximumSharpeOptimizer:

    def optimize(
        self,
        expected_returns,
        covariance,
        risk_free_rate=0.02,
    ):

        n = len(expected_returns)

        initial = np.ones(n) / n

        result = minimize(
            ObjectiveFunctions.negative_sharpe,
            initial,
            args=(
                expected_returns,
                covariance,
                risk_free_rate,
            ),
            method="SLSQP",
            bounds=Constraints.bounds(n),
            constraints=Constraints.weight_sum(),
        )

        if not result.success:
                    raise RuntimeError(result.message)
        
        return result.x