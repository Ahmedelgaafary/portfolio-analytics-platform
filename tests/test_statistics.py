"""
                        test_statistics.py

                        Part of Portfolio Analytics Platform.
                        """
import numpy as np
import pandas as pd

from src.statistics import (
    CorrelationCalculator,
    CovarianceCalculator,
    PortfolioStatistics,
    ReturnsCalculator,
)


def sample_prices():

    return pd.DataFrame(
        {
            "AAPL": [100, 102, 101, 105],
            "MSFT": [200, 203, 205, 208],
        }
    )


def test_simple_returns():

    calc = ReturnsCalculator()

    returns = calc.simple_returns(
        sample_prices()
    )

    assert not returns.empty


def test_covariance():

    returns = ReturnsCalculator().simple_returns(
        sample_prices()
    )

    cov = CovarianceCalculator().covariance_matrix(
        returns
    )

    assert cov.shape == (2, 2)


def test_correlation():

    returns = ReturnsCalculator().simple_returns(
        sample_prices()
    )

    corr = CorrelationCalculator().correlation_matrix(
        returns
    )

    assert corr.shape == (2, 2)


def test_portfolio_return():

    returns = ReturnsCalculator().simple_returns(
        sample_prices()
    )

    stats = PortfolioStatistics()

    expected = stats.expected_return(
        returns
    )

    weights = np.array([0.5, 0.5])

    value = stats.portfolio_return(
        weights,
        expected,
    )

    assert isinstance(value, float)