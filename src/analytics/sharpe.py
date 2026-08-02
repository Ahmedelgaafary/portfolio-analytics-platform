"""
                        sharpe.py

                        Part of Portfolio Analytics Platform.
                        
Sharpe Ratio.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


class SharpeRatio:

    def calculate(
        self,
        returns: pd.Series,
        risk_free_rate: float = 0.02,
        trading_days: int = 252,
    ) -> float:

        excess = (
            returns.mean() * trading_days
            - risk_free_rate
        )

        volatility = (
            returns.std()
            * np.sqrt(trading_days)
        )
        if volatility == 0:
            raise ValueError("Portfolio volatility is zero.")

        return float(excess / volatility)