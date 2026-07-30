"""
                        connection.py

                        Part of Portfolio Analytics Platform.                       

Database connection manager.

This module provides a single interface for connecting to the SQLite
database and executing SQL queries.
"""

from __future__ import annotations

import logging
import sqlite3
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class DatabaseManager:
    """
    Manage SQLite database connections and queries.

    Attributes
    ----------
    db_path : Path
        Path to the SQLite database file.
    connection : sqlite3.Connection | None
        Active SQLite connection.
    """

    def __init__(
        self,
        db_path: str | Path = "data/database.db",
    ) -> None:

        self.db_path = Path(db_path)

        # Ensure directory exists
        self.db_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.connection: sqlite3.Connection | None = None

    def connect(self) -> sqlite3.Connection:
        """
        Open a database connection.

        Returns
        -------
        sqlite3.Connection
            Active SQLite connection.
        """

        if self.connection is None:

            self.connection = sqlite3.connect(
                self.db_path
            )

            # Return rows as dictionaries
            self.connection.row_factory = sqlite3.Row

            logger.info(
                "Connected to database: %s",
                self.db_path,
            )

        return self.connection

    def close(self) -> None:
        """
        Close the database connection.
        """

        if self.connection is not None:

            self.connection.close()

            logger.info(
                "Database connection closed."
            )

            self.connection = None

    def execute(
        self,
        query: str,
        parameters: tuple[Any, ...] = (),
    ) -> None:
        """
        Execute INSERT, UPDATE or DELETE statements.

        Parameters
        ----------
        query : str
            SQL query.

        parameters : tuple
            SQL parameters.
        """

        conn = self.connect()

        try:

            conn.execute(
                query,
                parameters,
            )

            conn.commit()

        except sqlite3.Error as error:

            conn.rollback()

            logger.exception(
                "Database error: %s",
                error,
            )

            raise

    def executemany(
        self,
        query: str,
        parameters: list[tuple[Any, ...]],
    ) -> None:
        """
        Execute many INSERT statements.
        """

        conn = self.connect()

        try:

            conn.executemany(
                query,
                parameters,
            )

            conn.commit()

        except sqlite3.Error as error:

            conn.rollback()

            logger.exception(
                "Database error: %s",
                error,
            )

            raise

    def fetch_all(
        self,
        query: str,
        parameters: tuple[Any, ...] = (),
    ) -> list[sqlite3.Row]:
        """
        Execute SELECT and return all rows.
        """

        conn = self.connect()

        cursor = conn.execute(
            query,
            parameters,
        )

        return cursor.fetchall()

    def fetch_one(
        self,
        query: str,
        parameters: tuple[Any, ...] = (),
    ) -> sqlite3.Row | None:
        """
        Execute SELECT and return one row.
        """

        conn = self.connect()

        cursor = conn.execute(
            query,
            parameters,
        )

        return cursor.fetchone()

    def table_exists(
        self,
        table_name: str,
    ) -> bool:
        """
        Check whether a table exists.
        """

        query = """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name=?;
        """

        result = self.fetch_one(
            query,
            (table_name,),
        )

        return result is not None

    def __enter__(self):
        """
        Support context manager.
        """

        self.connect()

        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ):
        """
        Close connection automatically.
        """

        self.close()
                        
                        