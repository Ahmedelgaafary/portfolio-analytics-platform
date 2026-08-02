"""
                        sortino.py

                        Part of Portfolio Analytics Platform.
                       
Sortino Ratio.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


class SortinoRatio:

    def calculate(
        self,
        returns: pd.Series,
        risk_free_rate: float = 0.02,
        trading_days: int = 252,
    ) -> float:
        if returns.empty:
            raise ValueError("Return series is empty.")
        downside = returns[returns < 0]

        downside_std = (
            downside.std()
            * np.sqrt(trading_days)
        )
        if downside_std == 0 or np.isnan(downside_std):
             raise ValueError("Downside deviation is zero.")

        excess = (
            returns.mean() * trading_days
            - risk_free_rate
        )

        return float(excess / downside_std)