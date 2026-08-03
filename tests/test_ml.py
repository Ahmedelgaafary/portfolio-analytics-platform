"""
                        test_ml.py

                        Part of Portfolio Analytics Platform.
                        """

import pandas as pd

from src.ml.feature_engineering import (
    FeatureEngineer,
)


def sample_prices():

    return pd.DataFrame(
        {
            "Close": range(100, 150)
        }
    )


def test_feature_engineering():

    engineer = FeatureEngineer()

    df = engineer.create_features(
        sample_prices()
    )

    assert "MA5" in df.columns

    assert "Target" in df.columns

    assert len(df) > 0