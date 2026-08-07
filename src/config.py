"""
                        config.py

                        Part of Portfolio Analytics Platform.
                        
Application configuration.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Config:
    """
    Global application configuration.
    """

    # --------------------------------------------------
    # Project directories
    # --------------------------------------------------

    DATABASE_PATH: Path = Path(
        "data/database.db"
    )

    CACHE_DIRECTORY: Path = Path(
        "data/cache"
    )

    RAW_DATA_DIRECTORY: Path = Path(
        "data/raw"
    )

    PROCESSED_DATA_DIRECTORY: Path = Path(
        "data/processed"
    )

    EXPORT_DIRECTORY: Path = Path(
        "data/exports"
    )

    MODEL_DIRECTORY: Path = Path(
        "models"
    )

    REPORT_DIRECTORY: Path = Path(
        "reports"
    )

    FIGURE_DIRECTORY: Path = Path(
        "reports/figures"
    )

    PERFORMANCE_DIRECTORY: Path = Path(
        "reports/performance"
    )

    # --------------------------------------------------
    # Market data
    # --------------------------------------------------

    DEFAULT_START_DATE: str = "2018-01-01"

    DEFAULT_END_DATE: str = "2025-01-01"

    DEFAULT_INTERVAL: str = "1d"

    DEFAULT_TICKERS: tuple[str, ...] = (
        "AAPL",
        "MSFT",
        "GOOGL",
        "AMZN",
    )

    # --------------------------------------------------
    # Portfolio
    # --------------------------------------------------

    RISK_FREE_RATE: float = 0.02

    TRADING_DAYS: int = 252

    DEFAULT_OPTIMIZER: str = "maximum_sharpe"

    FRONTIER_POINTS: int = 100

    # --------------------------------------------------
    # Machine Learning
    # --------------------------------------------------

    TEST_SIZE: float = 0.20

    RANDOM_STATE: int = 42

    # --------------------------------------------------
    # Database
    # --------------------------------------------------

    DATABASE_TIMEOUT: int = 30

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------

    LOG_DIRECTORY: Path = Path(
        "logs"
    )

    LOG_FILE: str = "portfolio.log"

    LOG_LEVEL: str = "INFO"

    # --------------------------------------------------
    # Application
    # --------------------------------------------------

    APP_NAME: str = (
        "Portfolio Analytics Platform"
    )

    VERSION: str = "1.0.0"