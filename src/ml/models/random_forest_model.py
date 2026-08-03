"""
                        random_forest_model.py

                        Part of Portfolio Analytics Platform.
                        
Random Forest model.
"""

from sklearn.ensemble import RandomForestRegressor


class RandomForestModel:

    def build(self):

        return RandomForestRegressor(
            n_estimators=200,
            random_state=42,
            n_jobs=-1,
        )