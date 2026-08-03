"""
                        xgboost_model.py

                        Part of Portfolio Analytics Platform.
                        
XGBoost model.
"""

from xgboost import XGBRegressor


class XGBoostModel:

    def build(self):

        return XGBRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=5,
            random_state=42,
            n_jobs=-1,
        )