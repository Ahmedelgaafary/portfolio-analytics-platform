"""
                        test_optimization.py

                        Part of Portfolio Analytics Platform.
                        """
import numpy as np
import pandas as pd

from src.optimization import (
    EqualWeightOptimizer,
    MarkowitzOptimizer,
    MaximumSharpeOptimizer,
    MinimumVarianceOptimizer,
    OptimizerFactory,
)

def sample_data():

    expected_returns = pd.Series(
        [0.15, 0.10, 0.20]
    )

    covariance = pd.DataFrame(
        [
            [0.040, 0.006, 0.004],
            [0.006, 0.090, 0.008],
            [0.004, 0.008, 0.160],
        ]
    )

    return expected_returns, covariance


def test_equal_weight():

    weights = EqualWeightOptimizer().optimize(3)

    assert np.isclose(weights.sum(), 1.0)


def test_minimum_variance():

    _, cov = sample_data()

    weights = MinimumVarianceOptimizer().optimize(cov)

    assert np.isclose(weights.sum(), 1.0)


def test_maximum_sharpe():

    expected, cov = sample_data()

    weights = MaximumSharpeOptimizer().optimize(
        expected,
        cov,
    )

    assert np.isclose(weights.sum(), 1.0)


def test_markowitz():

    expected, cov = sample_data()

    weights = MarkowitzOptimizer().optimize(
        expected,
        cov,
    )

    assert np.isclose(weights.sum(), 1.0)


def test_factory():

    optimizer = OptimizerFactory.create(
        "markowitz"
    )

    assert optimizer is not None