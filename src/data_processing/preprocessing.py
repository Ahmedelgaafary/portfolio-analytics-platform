"""
                        preprocessing.py

                Part of Portfolio Analytics Platform.
                        
This module provides the DataPreprocessor class for validating,
cleaning, and preparing historical market data before it is used
by the statistics, optimization, machine learning, and
backtesting modules.
"""

from __future__ import annotations

import logging

import pandas as pd

logger = logging.getLogger(__name__)


class DataPreprocessor:
    """
    Preprocess historical market data.

    This class performs validation and cleaning operations on
    financial time series downloaded from external providers.
    """

    REQUIRED_COLUMNS = (
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
    )

    def validate_dataframe(
        self,
        df: pd.DataFrame,
    ) -> None:
        """
        Validate the input DataFrame.

        Args:
            df: Input market data.

        Raises:
            TypeError:
                If the input is not a pandas DataFrame.

            ValueError:
                If the DataFrame is empty.

            ValueError:
                If required columns are missing.
        """

        if not isinstance(df, pd.DataFrame):
            raise TypeError(
                "Input must be a pandas DataFrame."
            )

        if df.empty:
            raise ValueError(
                "Input DataFrame is empty."
            )

        missing_columns = [
            column
            for column in self.REQUIRED_COLUMNS
            if column not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

    def remove_duplicates(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Remove duplicate index values.

        Args:
            df: Input DataFrame.

        Returns:
            DataFrame without duplicated index values.
        """

        duplicates = df.index.duplicated().sum()

        if duplicates > 0:

            logger.warning(
                "Removed %d duplicated rows.",
                duplicates,
            )

            df = df.loc[~df.index.duplicated()]

        return df

    def sort_index(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Sort DataFrame by index.

        Args:
            df: Input DataFrame.

        Returns:
            Sorted DataFrame.
        """

        return df.sort_index()

    def fill_missing(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Fill missing values.

        Strategy:
            1. Forward fill
            2. Backward fill

        Args:
            df: Input DataFrame.

        Returns:
            DataFrame with missing values filled.
        """

        missing = int(df.isna().sum().sum())

        if missing > 0:

            logger.info(
                "Filling %d missing values.",
                missing,
            )

            df = df.ffill()
            df = df.bfill()

        return df

    def select_columns(
        self,
        df: pd.DataFrame,
        columns: list[str],
    ) -> pd.DataFrame:
        """
        Select a subset of columns.

        Args:
            df: Input DataFrame.
            columns: Columns to keep.

        Returns:
            Filtered DataFrame.
        """

        return df.loc[:, columns]

    def clean(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Execute the complete preprocessing pipeline.

        Pipeline:
            Validate
                ↓
            Remove duplicates
                ↓
            Sort index
                ↓
            Fill missing values

        Args:
            df: Raw market data.

        Returns:
            Cleaned DataFrame.
        """

        logger.info(
            "Starting data preprocessing."
        )

        self.validate_dataframe(df)

        df = self.remove_duplicates(df)

        df = self.sort_index(df)

        df = self.fill_missing(df)

        logger.info(
            "Data preprocessing completed."
        )

        return df