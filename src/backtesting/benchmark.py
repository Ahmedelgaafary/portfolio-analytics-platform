"""
                        benchmark.py

                        Part of Portfolio Analytics Platform.
Benchmark comparison.
"""

from __future__ import annotations

import pandas as pd


class Benchmark:
    """
    Benchmark performance.
    """

    def cumulative_return(
        self,
        benchmark_returns: pd.Series,
    ) -> float:

        return float((1 + benchmark_returns).prod()) - 1
        

    def excess_return(
        self,
        portfolio_returns: pd.Series,
        benchmark_returns: pd.Series,
    ) -> float:

        portfolio = float((1 + portfolio_returns).prod()) - 1
        

        benchmark = float((1 + benchmark_returns).prod()) - 1
        

        return (
            portfolio - benchmark
        )