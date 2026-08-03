"""
                        train.py

                        Part of Portfolio Analytics Platform.
                   
Training utilities.
"""

from __future__ import annotations


class ModelTrainer:

    def train(
        self,
        model,
        X_train,
        y_train,
    ):

        model.fit(
            X_train,
            y_train,
        )

        return model