"""
                        helpers.py

                        Part of Portfolio Analytics Platform.
                        
General helper functions.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path


class Helpers:

    @staticmethod
    def ensure_directory(
        directory: str | Path,
    ) -> Path:

        path = Path(directory)

        path.mkdir(
            parents=True,
            exist_ok=True,
        )

        return path

    @staticmethod
    def timestamp() -> str:

        return datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

    @staticmethod
    def file_exists(
        path: str | Path,
    ) -> bool:

        return Path(path).exists()

    @staticmethod
    def flatten_dict(
        dictionary: dict,
        parent_key: str = "",
        separator: str = ".",
    ) -> dict:

        items = []

        for key, value in dictionary.items():

            new_key = (
                f"{parent_key}{separator}{key}"
                if parent_key
                else key
            )

            if isinstance(
                value,
                dict,
            ):

                items.extend(
                    Helpers.flatten_dict(
                        value,
                        new_key,
                        separator,
                    ).items()
                )

            else:

                items.append(
                    (
                        new_key,
                        value,
                    )
                )

        return dict(items)