"""
                        dashboard.py

                        Part of Portfolio Analytics Platform.
Dashboard.
"""

from __future__ import annotations

from pprint import pprint


class Dashboard:
    """
    Console dashboard.
    """

    def display_metrics(
        self,
        metrics: dict,
    ) -> None:

        print("\nPortfolio Performance")
        print("=" * 40)

        for key, value in metrics.items():

            if key == "daily_returns":
                continue

            print(
                f"{key:<25}: {value}"
            )

    def display_weights(
        self,
        tickers,
        weights,
    ):

        print("\nPortfolio Allocation")
        print("=" * 40)

        for ticker, weight in zip(
            tickers,
            weights,
        ):

            print(
                f"{ticker:<10} {weight:.2%}"
            )

    def display_dictionary(
        self,
        data: dict,
    ):

        pprint(data)