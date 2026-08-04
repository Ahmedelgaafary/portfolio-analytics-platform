"""
                        test_backtesting.py

                        Part of Portfolio Analytics Platform.
                        """
import numpy as np
import pandas as pd

from src.backtesting.engine import (
    BacktestEngine,
)


def sample_returns():

    return pd.DataFrame(
        {
            "AAPL": [
                0.01,
                0.02,
                -0.01,
                0.01,
            ],
            "MSFT": [
                0.005,
                0.01,
                0.015,
                -0.02,
            ],
        }
    )


def test_backtest():

    engine = BacktestEngine()

    results = engine.run(
        sample_returns(),
        np.array([0.5, 0.5]),
    )

    assert "sharpe" in results

    assert "annual_return" in results

    assert "daily_returns" in results