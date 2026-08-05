"""
                        efficient_frontier.py

                        Part of Portfolio Analytics Platform.
                        

Efficient Frontier generation.
This module generates portfolios along the efficient frontier
and computes their expected return, volatility, and Sharpe ratio.
"""

from __future__ import annotations
import numpy as np
import pandas as pd

from src.statistics.portfolio_statistics import PortfolioStatistics

from .maximum_sharpe import MaximumSharpeOptimizer
from .minimum_variance import MinimumVarianceOptimizer


class EfficientFrontier:
    """
    Generate an approximation of the efficient frontier.
    """

    def generate(
        self,
        expected_returns: pd.Series,
        covariance: pd.DataFrame,
        risk_free_rate: float = 0.02,
        points: int = 100,
    ) -> dict:
        """
        Generate portfolios on the efficient frontier.

        Parameters
        ----------
        expected_returns : pd.Series
            Annual expected returns.

        covariance : pd.DataFrame
            Annual covariance matrix.

        risk_free_rate : float
            Annual risk-free rate.

        points : int
            Number of portfolios.

        Returns
        -------
        dict
            Dictionary containing:

            weights
            returns
            volatility
            sharpe
        """

        stats = PortfolioStatistics()

        min_weights = MinimumVarianceOptimizer().optimize(
            covariance
        )

        max_weights = MaximumSharpeOptimizer().optimize(
            expected_returns,
            covariance,
            risk_free_rate,
        )

        frontier_weights = []

        frontier_returns = []

        frontier_volatility = []

        frontier_sharpe = []

        for alpha in np.linspace(
            0.0,
            1.0,
            points,
        ):

            weights = (
                (1.0 - alpha) * min_weights
                + alpha * max_weights
            )

            weights = weights / np.sum(weights)

            portfolio_return = (
                stats.portfolio_return(
                    weights,
                    expected_returns,
                )
            )

            portfolio_volatility = (
                stats.portfolio_volatility(
                    weights,
                    covariance,
                )
            )

            if portfolio_volatility == 0:

                sharpe = 0.0

            else:

                sharpe = (
                    portfolio_return
                    - risk_free_rate
                ) / portfolio_volatility

            frontier_weights.append(weights)

            frontier_returns.append(
                portfolio_return
            )

            frontier_volatility.append(
                portfolio_volatility
            )

            frontier_sharpe.append(
                sharpe
            )

        return {
            "weights": frontier_weights,
            "returns": np.array(
                frontier_returns
            ),
            "volatility": np.array(
                frontier_volatility
            ),
            "sharpe": np.array(
                frontier_sharpe
            ),
        }