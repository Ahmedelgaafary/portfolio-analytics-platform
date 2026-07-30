"""
                        schema.py

                        Part of Portfolio Analytics Platform.
                        

Database schema initialization.

This module creates all database tables required by the
Portfolio Analytics Platform.
"""

from __future__ import annotations

import logging

from src.database.connection import DatabaseManager
from src.database.queries import (
    CREATE_BACKTEST_TABLE,
    CREATE_PORTFOLIO_TABLE,
    CREATE_PREDICTIONS_TABLE,
    CREATE_PRICES_TABLE,
)

logger = logging.getLogger(__name__)


class DatabaseSchema:
    """
    Create and initialize database tables.
    """

    def __init__(
        self,
        db: DatabaseManager,
    ) -> None:
        """
        Parameters
        ----------
        db : DatabaseManager
            Database connection manager.
        """
        self.db = db

    def create_tables(self) -> None:
        """
        Create all required database tables.
        """

        logger.info("Creating database tables...")

        self.db.execute(CREATE_PRICES_TABLE)

        self.db.execute(CREATE_PREDICTIONS_TABLE)

        self.db.execute(CREATE_PORTFOLIO_TABLE)

        self.db.execute(CREATE_BACKTEST_TABLE)

        logger.info("Database tables created successfully.")

    def drop_table(
        self,
        table_name: str,
    ) -> None:
        """
        Drop a table.

        Parameters
        ----------
        table_name : str
            Table name.
        """

        query = f"DROP TABLE IF EXISTS {table_name};"

        self.db.execute(query)

        logger.warning(
            "Dropped table: %s",
            table_name,
        )

    def drop_all_tables(self) -> None:
        """
        Drop every application table.

        Useful during development/testing.
        """

        tables = (
            "prices",
            "predictions",
            "portfolio",
            "backtests",
        )

        for table in tables:

            self.drop_table(table)

        logger.warning(
            "All database tables removed."
        )

    def reset_database(self) -> None:
        """
        Remove and recreate all tables.
        """

        logger.info(
            "Resetting database..."
        )

        self.drop_all_tables()

        self.create_tables()

        logger.info(
            "Database reset complete."
        )