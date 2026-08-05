"""
                        plots.py

                        Part of Portfolio Analytics Platform.
Plotting utilities.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


class Plotter:
    """
    Visualization helper.
    """

    def price_history(
        self,
        prices: pd.DataFrame,
        title: str = "Price History",
    ):

        ax = prices.plot(
            figsize=(12, 6),
            title=title,
        )

        ax.set_xlabel("Date")
        ax.set_ylabel("Price")

        plt.tight_layout()

        return ax

    def cumulative_returns(
        self,
        cumulative_returns: pd.Series,
        title: str = "Cumulative Returns",
    ):

        ax = cumulative_returns.plot(
            figsize=(12, 6),
            title=title,
        )

        ax.set_xlabel("Date")
        ax.set_ylabel("Return")

        plt.tight_layout()

        return ax

    def efficient_frontier(
        self,
        volatility,
        returns,
        sharpe=None,
    ):

        fig, ax = plt.subplots(figsize=(8, 6))

        scatter = ax.scatter(
            volatility,
            returns,
            c=sharpe if sharpe is not None else returns,
        )

        ax.set_xlabel("Volatility")
        ax.set_ylabel("Expected Return")
        ax.set_title("Efficient Frontier")

        plt.colorbar(scatter)

        plt.tight_layout()

        return ax