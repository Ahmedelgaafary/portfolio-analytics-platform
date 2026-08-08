"""
                        app.py

                        Part of Portfolio Analytics Platform.
Portfolio Analytics Platform.
Main application entry point.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.config import Config

from src.data_processing.downloader import (
    MarketDataDownloader,
)

from src.statistics.returns import (
    ReturnsCalculator,
)

from src.statistics.covariance import (
    CovarianceCalculator,
)

from src.statistics.portfolio_statistics import (
    PortfolioStatistics,
)

from src.optimization.optimizer_factory import (
    OptimizerFactory,
)

from src.optimization.efficient_frontier import (
    EfficientFrontier,
)

from src.backtesting.engine import (
    BacktestEngine,
)

from src.analytics.performance import (
    PerformanceAnalyzer,
)

from src.analytics.sharpe import (
    SharpeRatio,
)

from src.analytics.sortino import (
    SortinoRatio,
)

from src.analytics.drawdown import (
    DrawdownAnalyzer,
)

from src.analytics.var import (
    ValueAtRisk,
)

from src.analytics.cvar import (
    ConditionalValueAtRisk,
)

from src.visualization.dashboard import (
    Dashboard,
)

from src.visualization.plots import (
    Plotter,
)

from src.visualization.reports import (
    ReportGenerator,
)

from src.utils.logger import (
    setup_logger,
)

from src.utils.validators import (
    Validator,
)

from src.utils.helpers import (
    Helpers,
)

from src.utils.export import (
    Exporter,
)


def main() -> None:
    """
    Run the Portfolio Analytics Platform.
    """

    # --------------------------------------------------
    # Configuration
    # --------------------------------------------------

    config = Config()

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------

    logger = setup_logger(
        log_file=config.LOG_FILE,
    )

    logger.info(
        "Starting %s v%s",
        config.APP_NAME,
        config.VERSION,
    )

    # --------------------------------------------------
    # Create directories
    # --------------------------------------------------

    Helpers.ensure_directory(
        config.RAW_DATA_DIRECTORY
    )

    Helpers.ensure_directory(
        config.PROCESSED_DATA_DIRECTORY
    )

    Helpers.ensure_directory(
        config.CACHE_DIRECTORY
    )

    Helpers.ensure_directory(
        config.EXPORT_DIRECTORY
    )

    Helpers.ensure_directory(
        config.MODEL_DIRECTORY
    )

    Helpers.ensure_directory(
        config.REPORT_DIRECTORY
    )

    Helpers.ensure_directory(
        config.FIGURE_DIRECTORY
    )

    Helpers.ensure_directory(
        config.PERFORMANCE_DIRECTORY
    )

    # --------------------------------------------------
    # Validate configuration
    # --------------------------------------------------

    Validator.validate_tickers(
        list(config.DEFAULT_TICKERS)
    )

    Validator.validate_dates(
        config.DEFAULT_START_DATE,
        config.DEFAULT_END_DATE,
    )

    logger.info(
        "Configuration validated successfully"
    )

    # --------------------------------------------------
    # Market Data
    # --------------------------------------------------

    tickers = list(
        config.DEFAULT_TICKERS
    )

    logger.info(
        "Downloading market data for %s",
        tickers,
    )

    downloader = MarketDataDownloader(
        cache_dir=config.CACHE_DIRECTORY,
    )

    prices = downloader.download_multiple(
        tickers=tickers,
        start=config.DEFAULT_START_DATE,
        end=config.DEFAULT_END_DATE,
        interval=config.DEFAULT_INTERVAL,
    )
    
    Validator.validate_dataframe(
        prices
    )

    logger.info(
        "Market data downloaded successfully"
    )

    # --------------------------------------------------
    # Returns
    # --------------------------------------------------

    logger.info(
        "Calculating asset returns"
    )

    returns_calculator = ReturnsCalculator()

    returns = returns_calculator.simple_returns(
        prices
    )

    Validator.validate_dataframe(
        returns
    )

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    logger.info(
        "Calculating portfolio statistics"
    )

    covariance_calculator = (
        CovarianceCalculator()
    )

    covariance = (
        covariance_calculator
        .annualized_covariance(
            returns
        )
    )

    portfolio_statistics = (
        PortfolioStatistics()
    )

    expected_returns = (
        portfolio_statistics
        .expected_return(
            returns
        )
    )

    # --------------------------------------------------
    # Portfolio Optimization
    # --------------------------------------------------

    logger.info(
        "Running optimizer: %s",
        config.DEFAULT_OPTIMIZER,
    )

    optimizer = OptimizerFactory.create(
        config.DEFAULT_OPTIMIZER
    )

    if config.DEFAULT_OPTIMIZER == "equal_weight":

        weights = optimizer.optimize(
            len(tickers)
        )

    elif config.DEFAULT_OPTIMIZER == "minimum_variance":

        weights = optimizer.optimize(
            covariance
        )

    else:

        weights = optimizer.optimize(
            expected_returns,
            covariance,
            config.RISK_FREE_RATE,
        )

    weights = np.asarray(
        weights,
        dtype=float,
    )

    Validator.validate_weights(
        weights
    )

    logger.info(
        "Portfolio optimization completed"
    )

    # --------------------------------------------------
    # Efficient Frontier
    # --------------------------------------------------

    logger.info(
        "Generating efficient frontier"
    )

    frontier = EfficientFrontier().generate(
        expected_returns=expected_returns,
        covariance=covariance,
        risk_free_rate=config.RISK_FREE_RATE,
        points=config.FRONTIER_POINTS,
    )

    # --------------------------------------------------
    # Backtesting
    # --------------------------------------------------

    logger.info(
        "Running portfolio backtest"
    )

    backtest_engine = BacktestEngine()

    backtest_results = backtest_engine.run(
        asset_returns=returns,
        weights=weights,
    )

    portfolio_returns = (
        backtest_results["daily_returns"]
    )

    # --------------------------------------------------
    # Performance Analytics
    # --------------------------------------------------

    performance = PerformanceAnalyzer()

    sharpe = SharpeRatio()

    sortino = SortinoRatio()

    drawdown = DrawdownAnalyzer()

    var = ValueAtRisk()

    cvar = ConditionalValueAtRisk()

    metrics = {
        "annual_return":
            performance.annual_return(
                portfolio_returns,
                config.TRADING_DAYS,
            ),

        "annual_volatility":
            performance.annual_volatility(
                portfolio_returns,
                config.TRADING_DAYS,
            ),

        "cumulative_return":
            performance.cumulative_return(
                portfolio_returns,
            ),

        "sharpe_ratio":
            sharpe.calculate(
                portfolio_returns,
                config.RISK_FREE_RATE,
                config.TRADING_DAYS,
            ),

        "sortino_ratio":
            sortino.calculate(
                portfolio_returns,
                config.RISK_FREE_RATE,
                config.TRADING_DAYS,
            ),

        "maximum_drawdown":
            drawdown.maximum_drawdown(
                portfolio_returns,
            ),

        "value_at_risk":
            var.historical(
                portfolio_returns,
            ),

        "conditional_value_at_risk":
            cvar.historical(
                portfolio_returns,
            ),
    }

    # --------------------------------------------------
    # Dashboard
    # --------------------------------------------------

    dashboard = Dashboard()

    print()

    print("=" * 60)

    print(
        config.APP_NAME
    )

    print("=" * 60)

    dashboard.display_weights(
        tickers,
        weights,
    )

    dashboard.display_metrics(
        metrics,
    )

    # --------------------------------------------------
    # Export Portfolio Weights
    # --------------------------------------------------

    exporter = Exporter()

    weights_df = pd.DataFrame(
        {
            "ticker": tickers,
            "weight": weights,
        }
    )

    exporter.to_csv(
        weights_df,
        str(
            config.EXPORT_DIRECTORY
            / "portfolio_weights.csv"
        ),
    )

    # --------------------------------------------------
    # Export Performance Metrics
    # --------------------------------------------------

    exporter.to_csv(
        metrics,
        str(
            config.EXPORT_DIRECTORY
            / "performance_metrics.csv"
        ),
    )

    # --------------------------------------------------
    # Export Efficient Frontier
    # --------------------------------------------------

    frontier_df = pd.DataFrame(
        {
            "return": frontier["returns"],
            "volatility": frontier["volatility"],
            "sharpe": frontier["sharpe"],
        }
    )

    exporter.to_csv(
        frontier_df,
        str(
            config.EXPORT_DIRECTORY
            / "efficient_frontier.csv"
        ),
    )

    # --------------------------------------------------
    # Generate Report
    # --------------------------------------------------

    report_generator = ReportGenerator()

    report_generator.save_text_report(
        metrics,
        str(
            config.PERFORMANCE_DIRECTORY
            / "portfolio_report.txt"
        ),
    )

    # --------------------------------------------------
    # Visualization
    # --------------------------------------------------

    plotter = Plotter()

    plotter.price_history(
        prices,
        title="Asset Price History",
    )

    plotter.cumulative_returns(
        (
            1 + portfolio_returns
        ).cumprod(),
        title="Portfolio Cumulative Returns",
    )

    plotter.efficient_frontier(
        frontier["volatility"],
        frontier["returns"],
        frontier["sharpe"],
    )

    logger.info(
        "Results exported successfully"
    )

    logger.info(
        "Portfolio Analytics Platform completed"
    )

    print()
    print(
        "Application completed successfully."
    )


if __name__ == "__main__":
    main()