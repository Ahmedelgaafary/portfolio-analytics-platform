import pandas as pd

from src.visualization.plots import Plotter
from src.visualization.reports import ReportGenerator


def test_report(tmp_path):

    report = ReportGenerator()

    output = tmp_path / "report.txt"

    report.save_text_report(
        {
            "annual_return": 0.12,
            "sharpe": 1.45,
        },
        output,
    )

    assert output.exists()


def test_plot():

    prices = pd.DataFrame(
        {
            "AAPL": [100, 101, 102]
        }
    )

    plotter = Plotter()

    ax = plotter.price_history(
        prices
    )

    assert ax is not None