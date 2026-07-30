"""
                        test_database.py

                        Part of Portfolio Analytics Platform.
                        
Unit tests for the database layer.
"""

from __future__ import annotations

import pandas as pd

from src.database.connection import DatabaseManager
from src.database.models import (
    Backtest,
    Portfolio,
    Prediction,
)
from src.database.repository import Repository
from src.database.schema import DatabaseSchema


def create_repository(tmp_path):
    """
    Create a temporary repository for testing.
    """

    db = DatabaseManager(tmp_path / "test.db")

    schema = DatabaseSchema(db)

    schema.create_tables()

    repository = Repository(db)

    return repository


def sample_prices() -> pd.DataFrame:
    """
    Create sample historical prices.
    """

    return pd.DataFrame(
        {
            "Open": [100.0, 101.0, 102.0],
            "High": [101.0, 102.0, 103.0],
            "Low": [99.0, 100.0, 101.0],
            "Close": [100.5, 101.5, 102.5],
            "Volume": [1000, 1100, 1200],
        },
        index=pd.to_datetime(
            [
                "2024-01-01",
                "2024-01-02",
                "2024-01-03",
            ]
        ),
    )


# ==========================================================
# Connection
# ==========================================================


def test_database_connection(tmp_path):

    db = DatabaseManager(tmp_path / "test.db")

    conn = db.connect()

    assert conn is not None

    db.close()


# ==========================================================
# Schema
# ==========================================================


def test_tables_created(tmp_path):

    db = DatabaseManager(tmp_path / "test.db")

    schema = DatabaseSchema(db)

    schema.create_tables()

    assert db.table_exists("prices")

    assert db.table_exists("predictions")

    assert db.table_exists("portfolio")

    assert db.table_exists("backtests")

    db.close()


# ==========================================================
# Prices
# ==========================================================


def test_save_and_load_prices(tmp_path):

    repository = create_repository(tmp_path)

    prices = sample_prices()

    repository.save_prices(
        "AAPL",
        prices,
    )

    loaded = repository.load_prices(
        "AAPL",
    )

    assert len(loaded) == 3

    assert loaded.iloc[0]["Close"] == 100.5


def test_latest_price(tmp_path):

    repository = create_repository(tmp_path)

    repository.save_prices(
        "AAPL",
        sample_prices(),
    )

    latest = repository.latest_price(
        "AAPL",
    )

    assert latest is not None


# ==========================================================
# Prediction
# ==========================================================


def test_prediction(tmp_path):

    repository = create_repository(tmp_path)

    prediction = Prediction(
        ticker="AAPL",
        date="2024-01-04",
        prediction=105.2,
        confidence=0.91,
        model="RandomForest",
    )

    repository.save_prediction(
        prediction,
    )

    predictions = repository.load_predictions(
        "AAPL",
    )

    assert len(predictions) == 1


# ==========================================================
# Portfolio
# ==========================================================


def test_portfolio(tmp_path):

    repository = create_repository(tmp_path)

    portfolio = [
        Portfolio(
            ticker="AAPL",
            weight=0.60,
        ),
        Portfolio(
            ticker="MSFT",
            weight=0.40,
        ),
    ]

    repository.save_portfolio(
        portfolio,
    )

    loaded = repository.load_portfolio()

    assert len(loaded) == 2


# ==========================================================
# Backtests
# ==========================================================


def test_backtest(tmp_path):

    repository = create_repository(tmp_path)

    result = Backtest(
        strategy="Maximum Sharpe",
        annual_return=0.18,
        sharpe=1.42,
        max_drawdown=-0.12,
    )

    repository.save_backtest(
        result,
    )

    backtests = repository.load_backtests()

    assert len(backtests) == 1