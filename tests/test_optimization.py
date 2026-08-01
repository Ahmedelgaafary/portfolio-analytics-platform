"""
                        test_optimization.py

                        Part of Portfolio Analytics Platform.
                        """
import numpy as np
import pandas as pd

from src.optimization import (
    EqualWeightOptimizer,
    MinimumVarianceOptimizer,
)


def sample_covariance():

    return pd.DataFrame(
        [
            [0.10, 0.02],
            [0.02, 0.08],
        ]
    )


def test_equal_weight():

    optimizer = EqualWeightOptimizer()

    weights = optimizer.optimize(2)

    assert np.isclose(
        weights.sum(),
        1.0,
    )


def test_minimum_variance():

    optimizer = MinimumVarianceOptimizer()

    weights = optimizer.optimize(
        sample_covariance()
    )

    assert np.isclose(
        weights.sum(),
        1.0,
    )