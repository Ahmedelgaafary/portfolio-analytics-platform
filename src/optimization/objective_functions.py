"""
                        objective_functions.py

                        Part of Portfolio Analytics Platform.
                        

Objective functions.
"""

from __future__ import annotations

import numpy as np


class ObjectiveFunctions:

    @staticmethod
    def portfolio_variance(
        weights,
        covariance,
    ):

        return (
            weights.T
            @ covariance.values
            @ weights
        )

    @staticmethod
    def negative_sharpe(
        weights,
        expected_returns,
        covariance,
        risk_free_rate=0.02,
    ):

        portfolio_return = np.dot(
            weights,
            expected_returns,
        )

        portfolio_volatility = np.sqrt(
            weights.T
            @ covariance.values
            @ weights
        )

        return -(
            (
                portfolio_return
                - risk_free_rate
            )
            / portfolio_volatility
        )