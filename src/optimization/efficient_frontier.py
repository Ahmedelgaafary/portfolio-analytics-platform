"""
                        efficient_frontier.py

                        Part of Portfolio Analytics Platform.
                        

Efficient Frontier.
"""

from __future__ import annotations

import numpy as np

from .maximum_sharpe import MaximumSharpeOptimizer
from .minimum_variance import MinimumVarianceOptimizer


class EfficientFrontier:

    def generate(
        self,
        expected_returns,
        covariance,
        points=50,
    ):

        minimum = MinimumVarianceOptimizer().optimize(
            covariance
        )

        maximum = MaximumSharpeOptimizer().optimize(
            expected_returns,
            covariance,
        )

        frontier = []

        for alpha in np.linspace(
            0,
            1,
            points,
        ):

            weights = (
                (1 - alpha)
                * minimum
                + alpha
                * maximum
            )

            frontier.append(weights)

        return frontier