"""
                        logger.py

                        Part of Portfolio Analytics Platform.
Logging utilities.
"""

from __future__ import annotations

import logging
from pathlib import Path


def setup_logger(
    name: str = "portfolio_analytics",
    log_file: str = "portfolio.log",
    level: int = logging.INFO,
) -> logging.Logger:
    """
    Configure application logger.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(level)

    Path("logs").mkdir(
        parents=True,
        exist_ok=True,
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        Path("logs") / log_file,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger