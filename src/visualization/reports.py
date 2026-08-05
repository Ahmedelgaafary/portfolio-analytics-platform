"""
                        reports.py

                        Part of Portfolio Analytics Platform.
Report generation.
"""

from __future__ import annotations

from pathlib import Path


class ReportGenerator:
    """
    Export reports.
    """

    def save_text_report(
        self,
        metrics: dict,
        output_path: str,
    ) -> None:

        path = Path(output_path)

        with path.open(
            "w",
            encoding="utf-8",
        ) as file:

            file.write(
                "Portfolio Analytics Report\n"
            )

            file.write("=" * 40)

            file.write("\n\n")

            for key, value in metrics.items():

                if key == "daily_returns":
                    continue

                file.write(
                    f"{key}: {value}\n"
                )