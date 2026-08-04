"""
                        engine.py

                        Part of Portfolio Analytics Platform.
                        
Backtesting engine.
"""

from __future__ import annotations

import pandas as pd

from src.analytics.performance import PerformanceAnalyzer
from src.analytics.sharpe import SharpeRatio
from src.analytics.drawdown import DrawdownAnalyzer

from .portfolio import Portfolio


class BacktestEngine:
    """
    Execute historical portfolio backtests.
    """

    def run(
        self,
        asset_returns: pd.DataFrame,
        weights,
    ) -> dict:

        portfolio = Portfolio(weights)

        returns = portfolio.returns(
            asset_returns
        )

        performance = PerformanceAnalyzer()

        sharpe = SharpeRatio()

        drawdown = DrawdownAnalyzer()

        return {
            "annual_return":
                performance.annual_return(
                    returns
                ),
            "annual_volatility":
                performance.annual_volatility(
                    returns
                ),
            "cumulative_return":
                performance.cumulative_return(
                    returns
                ),
            "sharpe":
                sharpe.calculate(
                    returns
                ),
            "max_drawdown":
                drawdown.maximum_drawdown(
                    returns
                ),
            "daily_returns":
                returns,
        }