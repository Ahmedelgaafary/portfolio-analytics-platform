"""
                        test_integration.py

                        Part of Portfolio Analytics Platform.
                        
Integration tests for the Portfolio Analytics Platform.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.analytics.performance import PerformanceAnalyzer
from src.backtesting.engine import BacktestEngine
from src.optimization.efficient_frontier import EfficientFrontier
from src.optimization.optimizer_factory import OptimizerFactory
from src.statistics.covariance import CovarianceCalculator
from src.statistics.portfolio_statistics import PortfolioStatistics
from src.statistics.returns import ReturnsCalculator


def create_sample_prices() -> pd.DataFrame:
    """
    Create deterministic sample market prices.
    """

    dates = pd.date_range(
        start="2024-01-01",
        periods=100,
        freq="D",
    )

    np.random.seed(42)

    returns = np.random.normal(
        0.0005,
        0.01,
        size=(100, 3),
    )

    prices = 100 * np.exp(
        np.cumsum(returns, axis=0)
    )

    return pd.DataFrame(
        prices,
        index=dates,
        columns=[
            "ASSET_A",
            "ASSET_B",
            "ASSET_C",
        ],
    )


def test_full_portfolio_pipeline():
    """
    Test the complete:

    Prices
        ↓
    Returns
        ↓
    Statistics
        ↓
    Optimization
        ↓
    Backtesting
        ↓
    Performance
    """

    # ----------------------------------------------
    # 1. Market data
    # ----------------------------------------------

    prices = create_sample_prices()

    assert not prices.empty

    assert prices.shape == (100, 3)

    # ----------------------------------------------
    # 2. Returns
    # ----------------------------------------------

    returns_calculator = ReturnsCalculator()

    returns = returns_calculator.simple_returns(
        prices
    )

    assert not returns.empty

    assert returns.shape[1] == 3

    # ----------------------------------------------
    # 3. Statistics
    # ----------------------------------------------

    covariance_calculator = (
        CovarianceCalculator()
    )

    covariance = (
        covariance_calculator
        .annualized_covariance(
            returns
        )
    )

    assert covariance.shape == (3, 3)

    portfolio_statistics = (
        PortfolioStatistics()
    )

    expected_returns = (
        portfolio_statistics
        .expected_return(
            returns
        )
    )

    assert len(expected_returns) == 3

    # ----------------------------------------------
    # 4. Optimization
    # ----------------------------------------------

    optimizer = OptimizerFactory.create(
        "maximum_sharpe"
    )

    weights = optimizer.optimize(
        expected_returns,
        covariance,
        risk_free_rate=0.02,
    )

    assert len(weights) == 3

    assert np.isclose(
        weights.sum(),
        1.0,
        atol=1e-6,
    )

    assert np.all(weights >= 0)

    # ----------------------------------------------
    # 5. Efficient Frontier
    # ----------------------------------------------

    frontier = EfficientFrontier().generate(
        expected_returns=expected_returns,
        covariance=covariance,
        risk_free_rate=0.02,
        points=20,
    )

    assert "weights" in frontier

    assert "returns" in frontier

    assert "volatility" in frontier

    assert "sharpe" in frontier

    assert len(frontier["returns"]) == 20

    assert len(frontier["volatility"]) == 20

    assert len(frontier["sharpe"]) == 20

    # ----------------------------------------------
    # 6. Backtesting
    # ----------------------------------------------

    engine = BacktestEngine()

    results = engine.run(
        asset_returns=returns,
        weights=weights,
    )

    assert "annual_return" in results

    assert "annual_volatility" in results

    assert "cumulative_return" in results

    assert "sharpe" in results

    assert "max_drawdown" in results

    assert "daily_returns" in results

    # ----------------------------------------------
    # 7. Performance
    # ----------------------------------------------

    performance = PerformanceAnalyzer()

    portfolio_returns = (
        results["daily_returns"]
    )

    annual_return = (
        performance.annual_return(
            portfolio_returns
        )
    )

    annual_volatility = (
        performance.annual_volatility(
            portfolio_returns
        )
    )

    cumulative_return = (
        performance.cumulative_return(
            portfolio_returns
        )
    )

    assert isinstance(
        annual_return,
        float,
    )

    assert isinstance(
        annual_volatility,
        float,
    )

    assert isinstance(
        cumulative_return,
        float,
    )

    assert annual_volatility >= 0