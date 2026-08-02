"""
                        drawdown.py

                        Part of Portfolio Analytics Platform.
                        
Drawdown calculations.
"""

from __future__ import annotations

import pandas as pd


class DrawdownAnalyzer:

    def drawdown(
        self,
        returns: pd.Series,
    ) -> pd.Series:
        if returns.empty:
            raise ValueError("Return series is empty.")

        wealth = (1 + returns).cumprod()

        peak = wealth.cummax()

        return (wealth - peak) / peak

    def maximum_drawdown(
        self,
        returns: pd.Series,
    ) -> float:
        if returns.empty:
            raise ValueError("Return series is empty.")

        return float(
            self.drawdown(
                returns
            ).min()
        )