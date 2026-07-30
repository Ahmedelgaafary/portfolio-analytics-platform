"""
                        models.py

                        Part of Portfolio Analytics Platform.

Database models.

This module defines the data models used throughout the
Portfolio Analytics Platform.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Price:
    """
    Historical market price.
    """

    ticker: str
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int


@dataclass(slots=True)
class Prediction:
    """
    Machine learning prediction.
    """

    ticker: str
    date: str
    prediction: float
    confidence: float
    model: str


@dataclass(slots=True)
class Portfolio:
    """
    Portfolio holding.
    """

    ticker: str
    weight: float


@dataclass(slots=True)
class Backtest:
    """
    Backtest result.
    """

    strategy: str
    annual_return: float
    sharpe: float
    max_drawdown: float