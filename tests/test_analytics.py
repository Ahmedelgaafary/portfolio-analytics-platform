"""
                        test_analytics.py

                        Part of Portfolio Analytics Platform.
"""

import pandas as pd

from src.analytics import (
    ConditionalValueAtRisk,
    DrawdownAnalyzer,
    PerformanceAnalyzer,
    SharpeRatio,
    SortinoRatio,
    ValueAtRisk,
)


def sample_returns():

    return pd.Series(
        [
            0.01,
            -0.02,
            0.03,
            0.015,
            -0.01,
            0.02,
        ]
    )


def test_performance():

    analyzer = PerformanceAnalyzer()

    value = analyzer.annual_return(
        sample_returns()
    )

    assert isinstance(value, float)


def test_sharpe():

    value = SharpeRatio().calculate(
        sample_returns()
    )

    assert isinstance(value, float)


def test_sortino():

    value = SortinoRatio().calculate(
        sample_returns()
    )

    assert isinstance(value, float)


def test_drawdown():

    value = DrawdownAnalyzer().maximum_drawdown(
        sample_returns()
    )

    assert value <= 0


def test_var():

    value = ValueAtRisk().historical(
        sample_returns()
    )

    assert isinstance(value, float)


def test_cvar():

    value = ConditionalValueAtRisk().historical(
        sample_returns()
    )

    assert isinstance(value, float)