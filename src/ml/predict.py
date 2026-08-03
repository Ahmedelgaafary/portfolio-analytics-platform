"""
                        predict.py

                        Part of Portfolio Analytics Platform.
                        
Prediction utilities.
"""

from __future__ import annotations


class Predictor:

    def predict(
        self,
        model,
        X,
    ):

        return model.predict(X)