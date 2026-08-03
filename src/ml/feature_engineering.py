"""
                        feature_engineering.py

                        Part of Portfolio Analytics Platform.
                        
Feature engineering.
"""

from __future__ import annotations

import pandas as pd


class FeatureEngineer:

    def create_features(
        self,
        prices: pd.DataFrame,
    ) -> pd.DataFrame:

        df = prices.copy()

        df["Return"] = df["Close"].pct_change()

        df["MA5"] = (
            df["Close"]
            .rolling(5)
            .mean()
        )

        df["MA20"] = (
            df["Close"]
            .rolling(20)
            .mean()
        )

        df["Volatility"] = (
            df["Return"]
            .rolling(20)
            .std()
        )

        df["Momentum"] = (
            df["Close"]
            - df["Close"].shift(5)
        )

        df["Target"] = (
            df["Return"].shift(-1)
        )

        return df.dropna()