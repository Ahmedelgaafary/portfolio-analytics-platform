"""
                        var.py

                        Part of Portfolio Analytics Platform.
                        
Value at Risk.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


class ValueAtRisk:

    def historical(
        self,
        returns: pd.Series,
        confidence: float = 0.95,
    ) -> float:

        percentile = (
            1 - confidence
        ) * 100

        return float(
            np.percentile(
                returns,
                percentile,
            )
        )