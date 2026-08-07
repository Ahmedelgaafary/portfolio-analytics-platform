"""
                        validators.py

                        Part of Portfolio Analytics Platform.
                        
Validation utilities.
"""

from __future__ import annotations

from datetime import datetime

import numpy as np
import pandas as pd


class Validator:

    @staticmethod
    def validate_dataframe(
        df: pd.DataFrame,
    ) -> None:

        if df.empty:
            raise ValueError(
                "DataFrame is empty."
            )

    @staticmethod
    def validate_weights(
        weights,
        tolerance: float = 1e-6,
    ) -> None:

        if not np.isclose(
            np.sum(weights),
            1.0,
            atol=tolerance,
        ):
            raise ValueError(
                "Portfolio weights must sum to 1."
            )

    @staticmethod
    def validate_dates(
        start: str,
        end: str,
    ) -> None:

        try:
            start_date = datetime.fromisoformat(start)
            end_date = datetime.fromisoformat(end)

        except ValueError as exc:
            raise ValueError(
                "Dates must be in YYYY-MM-DD format."
            ) from exc

        if start_date >= end_date:
            raise ValueError(
                "Start date must be before end date."
            )

    @staticmethod
    def validate_tickers(
        tickers: list[str],
    ) -> None:

        if len(tickers) == 0:
            raise ValueError(
                "Ticker list is empty."
            )

        for ticker in tickers:

            if not ticker.strip():
                raise ValueError(
                    "Ticker cannot be empty."
                )