"""
                        preprocessing.py

                        Part of Portfolio Analytics Platform.
                        
Machine learning preprocessing.
"""

from __future__ import annotations

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class MLPreprocessor:

    FEATURES = [
        "MA5",
        "MA20",
        "Volatility",
        "Momentum",
    ]

    TARGET = "Target"

    def prepare(
        self,
        df: pd.DataFrame,
        test_size: float = 0.2,
    ):

        X = df[self.FEATURES]

        y = df[self.TARGET]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            shuffle=False,
            test_size=test_size,
        )

        scaler = StandardScaler()

        X_train = scaler.fit_transform(
            X_train
        )

        X_test = scaler.transform(
            X_test
        )

        return (
            X_train,
            X_test,
            y_train,
            y_test,
            scaler,
        )