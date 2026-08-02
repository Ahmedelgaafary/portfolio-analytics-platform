"""
                        cvar.py

                        Part of Portfolio Analytics Platform.
                        
Conditional Value at Risk.
"""

from __future__ import annotations

import pandas as pd

from .var import ValueAtRisk


class ConditionalValueAtRisk:

    def historical(
        self,
        returns: pd.Series,
        confidence: float = 0.95,
    ) -> float:

        var = ValueAtRisk().historical(
            returns,
            confidence,
        )

        return float(
            returns[
                returns <= var
            ].mean()
        )