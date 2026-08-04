"""
                        portfolio.py

                        Part of Portfolio Analytics Platform.
                        
Portfolio representation.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(slots=True)
class Portfolio:
    """
    Portfolio with asset weights.
    """

    weights: np.ndarray

    def returns(
        self,
        asset_returns: pd.DataFrame,
    ) -> pd.Series:
        """
        Calculate portfolio returns.
        """

        return asset_returns @ self.weights

    def cumulative_returns(
        self,
        asset_returns: pd.DataFrame,
    ) -> pd.Series:
        """
        Calculate cumulative portfolio returns.
        """

        returns = self.returns(asset_returns)

        return (1 + returns).cumprod()