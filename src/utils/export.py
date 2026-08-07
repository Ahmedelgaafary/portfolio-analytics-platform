"""
                        export.py

                        Part of Portfolio Analytics Platform.
Export utilities.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

class Exporter:
    """
    Export data to CSV, Excel, or JSON files.
    """

    def to_csv(
        self,
        data,
        output_file: str,
    ) -> None:
        """
        Export a DataFrame or dictionary to CSV.
        """

        Path(output_file).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if isinstance(
            data,
            pd.DataFrame,
        ):

            data.to_csv(
                output_file,
                index=True,
            )

        elif isinstance(
            data,
            dict,
        ):

            pd.DataFrame(
                [data]
            ).to_csv(
                output_file,
                index=False,
            )

        else:

            raise TypeError(
                "Data must be a pandas DataFrame or dictionary."
            )

    def to_excel(
        self,
        data: pd.DataFrame,
        output_file: str,
    ) -> None:
        """
        Export a DataFrame to Excel.
        """

        Path(output_file).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not isinstance(
            data,
            pd.DataFrame,
        ):
            raise TypeError(
                "Data must be a pandas DataFrame."
            )

        data.to_excel(
            output_file,
            index=True,
        )

    def to_json(
        self,
        data,
        output_file: str,
    ) -> None:
        """
        Export a DataFrame or dictionary to JSON.
        """

        Path(output_file).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if isinstance(
            data,
            pd.DataFrame,
        ):

            data.to_json(
                output_file,
                orient="records",
                indent=4,
            )

        elif isinstance(
            data,
            dict,
        ):

            pd.Series(
                data
            ).to_json(
                output_file,
                indent=4,
            )

        else:

            raise TypeError(
                "Data must be a pandas DataFrame or dictionary."
            )
