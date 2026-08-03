"""
                        evaluation.py

                        Part of Portfolio Analytics Platform.
                        
Model evaluation.
"""

from __future__ import annotations

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    root_mean_squared_error,
    r2_score,
)


class Evaluator:

    def regression_metrics(
        self,
        y_true,
        y_pred,
    ):

        return {
            "MAE": mean_absolute_error(
                y_true,
                y_pred,
            ),
            "MSE": mean_squared_error(
                y_true,
                y_pred,
            ),
            "RMSE": root_mean_squared_error(
                y_true,
                y_pred,
            ),
            "R2": r2_score(
                y_true,
                y_pred,
            ),
        }