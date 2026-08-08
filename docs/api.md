# Api
# Portfolio Analytics Platform — API Reference

## 1. Overview

This document describes the main Python modules and classes available in the Portfolio Analytics Platform.

The API is organized according to the project architecture:

```text
Data Processing
Database
Statistics
Optimization
Machine Learning
Analytics
Backtesting
Visualization
Utilities
```

---

# 2. Data Processing API

## `src.data_processing.downloader`

### `MarketDataDownloader`

Downloads historical market data.

```python
from src.data_processing.downloader import MarketDataDownloader
```

Example:

```python
downloader = MarketDataDownloader(
    cache_dir="data/cache"
)

data = downloader.download(
    ticker="AAPL",
    start="2020-01-01",
    end="2025-01-01",
)
```

---

## `src.data_processing.preprocessing`

Provides market-data preprocessing functions.

Typical operations include:

* Missing-value handling
* Data cleaning
* Column normalization
* Data preparation

---

## `src.data_processing.cache`

### `CacheManager`

Handles local storage and retrieval of cached datasets.

Example:

```python
from src.data_processing.cache import CacheManager

cache = CacheManager(
    cache_dir="data/cache"
)
```

---

## `src.data_processing.loaders`

Provides functions for loading stored datasets.

---

# 3. Database API

## `src.database.connection`

Provides database connection management.

---

## `src.database.schema`

Defines the database schema used by the application.

---

## `src.database.models`

Contains application database models.

---

## `src.database.repository`

Provides the repository layer for database operations.

Typical operations include:

```text
Create
Read
Update
Delete
```

---

## `src.database.queries`

Contains reusable database queries.

---

# 4. Statistics API

## `src.statistics.returns`

### `ReturnsCalculator`

Calculates asset returns.

Example:

```python
from src.statistics.returns import ReturnsCalculator

calculator = ReturnsCalculator()

returns = calculator.simple_returns(
    prices
)
```

---

## `src.statistics.covariance`

### `CovarianceCalculator`

Calculates covariance matrices.

Example:

```python
from src.statistics.covariance import CovarianceCalculator

calculator = CovarianceCalculator()

covariance = calculator.annualized_covariance(
    returns
)
```

---

## `src.statistics.correlation`

Provides correlation calculations.

---

## `src.statistics.portfolio_statistics`

### `PortfolioStatistics`

Provides portfolio-level statistical calculations.

Typical calculations include:

```text
Expected Return
Portfolio Return
Portfolio Volatility
Portfolio Variance
```

Example:

```python
from src.statistics.portfolio_statistics import (
    PortfolioStatistics,
)

stats = PortfolioStatistics()

portfolio_return = stats.portfolio_return(
    weights,
    expected_returns,
)

volatility = stats.portfolio_volatility(
    weights,
    covariance,
)
```

---

# 5. Optimization API

## `src.optimization.equal_weight`

### `EqualWeightOptimizer`

Creates an equally weighted portfolio.

Example:

```python
from src.optimization.equal_weight import (
    EqualWeightOptimizer,
)

optimizer = EqualWeightOptimizer()

weights = optimizer.optimize(
    number_of_assets
)
```

---

## `src.optimization.minimum_variance`

### `MinimumVarianceOptimizer`

Minimizes portfolio variance.

Example:

```python
from src.optimization.minimum_variance import (
    MinimumVarianceOptimizer,
)

optimizer = MinimumVarianceOptimizer()

weights = optimizer.optimize(
    covariance
)
```

---

## `src.optimization.maximum_sharpe`

### `MaximumSharpeOptimizer`

Maximizes the Sharpe ratio.

Example:

```python
from src.optimization.maximum_sharpe import (
    MaximumSharpeOptimizer,
)

optimizer = MaximumSharpeOptimizer()

weights = optimizer.optimize(
    expected_returns,
    covariance,
    risk_free_rate=0.02,
)
```

---

## `src.optimization.markowitz`

### `MarkowitzOptimizer`

Provides Markowitz portfolio optimization.

Example:

```python
from src.optimization.markowitz import (
    MarkowitzOptimizer,
)

optimizer = MarkowitzOptimizer()

weights = optimizer.optimize(
    expected_returns,
    covariance,
)
```

---

## `src.optimization.optimizer_factory`

### `OptimizerFactory`

Creates an optimizer from a string identifier.

Example:

```python
from src.optimization.optimizer_factory import (
    OptimizerFactory,
)

optimizer = OptimizerFactory.create(
    "maximum_sharpe"
)
```

Available optimizers:

```text
equal_weight
minimum_variance
maximum_sharpe
markowitz
```

---

# 6. Efficient Frontier API

## `src.optimization.efficient_frontier`

### `EfficientFrontier`

Generates a set of portfolios representing the risk-return relationship.

Example:

```python
from src.optimization.efficient_frontier import (
    EfficientFrontier,
)

frontier = EfficientFrontier().generate(
    expected_returns=expected_returns,
    covariance=covariance,
    risk_free_rate=0.02,
    points=100,
)
```

The returned dictionary contains:

```python
{
    "weights": ...,
    "returns": ...,
    "volatility": ...,
    "sharpe": ...,
}
```

This allows the visualization layer to plot:

```text
Volatility
    vs
Return
```

while also identifying the Sharpe ratio for each generated portfolio.

---

# 7. Machine Learning API

## `src.ml.feature_engineering`

Provides functions for creating machine-learning features from financial data.

Typical features may include:

```text
Returns
Moving averages
Volatility
Momentum
Lagged variables
```

---

## `src.ml.preprocessing`

Prepares ML datasets for training.

---

## `src.ml.train`

Provides model-training functionality.

---

## `src.ml.predict`

Provides prediction functionality.

---

## `src.ml.evaluation`

Provides model evaluation metrics.

---

## `src.ml.models.xgboost_model`

Provides the XGBoost model implementation.

---

## `src.ml.models.random_forest_model`

Provides the Random Forest model implementation.

---

# 8. Analytics API

## `src.analytics.performance`

### `PerformanceAnalyzer`

Calculates portfolio performance metrics.

Typical metrics:

```text
Annual Return
Annual Volatility
Cumulative Return
```

Example:

```python
from src.analytics.performance import (
    PerformanceAnalyzer,
)

analyzer = PerformanceAnalyzer()

annual_return = analyzer.annual_return(
    portfolio_returns
)
```

---

## `src.analytics.sharpe`

### `SharpeRatio`

Calculates the Sharpe ratio.

```python
from src.analytics.sharpe import SharpeRatio

sharpe = SharpeRatio()

ratio = sharpe.calculate(
    portfolio_returns,
    risk_free_rate=0.02,
)
```

---

## `src.analytics.sortino`

### `SortinoRatio`

Calculates the Sortino ratio.

---

## `src.analytics.drawdown`

### `DrawdownAnalyzer`

Calculates portfolio drawdowns.

Typical metrics:

```text
Drawdown
Maximum Drawdown
```

---

## `src.analytics.var`

### `ValueAtRisk`

Calculates Value at Risk.

Supported approaches depend on the implementation in the module.

---

## `src.analytics.cvar`

### `ConditionalValueAtRisk`

Calculates Conditional Value at Risk.

---

# 9. Backtesting API

## `src.backtesting.engine`

### `BacktestEngine`

Runs historical portfolio simulations.

Example:

```python
from src.backtesting.engine import BacktestEngine

engine = BacktestEngine()

results = engine.run(
    asset_returns=returns,
    weights=weights,
)
```

The result contains portfolio performance information including:

```text
Daily Returns
Annual Return
Annual Volatility
Cumulative Return
Sharpe Ratio
Maximum Drawdown
```

---

## `src.backtesting.portfolio`

Provides portfolio construction functionality.

---

## `src.backtesting.rebalancing`

Provides portfolio rebalancing functionality.

---

## `src.backtesting.benchmark`

Provides benchmark comparison functionality.

---

# 10. Visualization API

## `src.visualization.plots`

### `Plotter`

Creates analytical plots.

Examples:

```python
from src.visualization.plots import Plotter

plotter = Plotter()

plotter.price_history(
    prices
)

plotter.cumulative_returns(
    cumulative_returns
)

plotter.efficient_frontier(
    volatility,
    returns,
    sharpe,
)
```

---

## `src.visualization.dashboard`

### `Dashboard`

Displays portfolio information and metrics.

---

## `src.visualization.reports`

### `ReportGenerator`

Generates portfolio reports.

---

# 11. Utilities API

## `src.utils.logger`

### `setup_logger`

Creates the application logger.

```python
from src.utils.logger import setup_logger

logger = setup_logger()

logger.info(
    "Application started"
)
```

---

## `src.utils.validators`

### `Validator`

Provides validation functions.

Example:

```python
Validator.validate_dataframe(
    data
)

Validator.validate_weights(
    weights
)

Validator.validate_tickers(
    tickers
)
```

---

## `src.utils.export`

### `Exporter`

Exports results.

Example:

```python
from src.utils.export import Exporter

exporter = Exporter()

exporter.to_csv(
    dataframe,
    "data/exports/results.csv",
)
```

---

## `src.utils.helpers`

### `Helpers`

Provides general helper functions.

Example:

```python
from src.utils.helpers import Helpers

Helpers.ensure_directory(
    "data/exports"
)
```

---

# 12. Configuration API

## `src.config`

### `Config`

Contains application configuration.

Example:

```python
from src.config import Config

config = Config()

print(
    config.RISK_FREE_RATE
)

print(
    config.DEFAULT_TICKERS
)
```

---

# 13. Application API

## `src.app`

### `main`

Runs the complete platform.

Example:

```bash
python -m src.app
```

The main application coordinates:

```text
Data
 ↓
Statistics
 ↓
Optimization
 ↓
Backtesting
 ↓
Analytics
 ↓
Visualization
 ↓
Export
```

---

# 14. Testing API

Tests are executed using `pytest`.

Run all tests:

```bash
py -m pytest -v
```

Run a specific test module:

```bash
py -m pytest tests/test_optimization.py -v
```

Run integration tests:

```bash
py -m pytest tests/test_integration.py -v
```

---

# 15. Output Files

The application generates analytical outputs under:

```text
data/exports/
```

Typical files include:

```text
portfolio_weights.csv
performance_metrics.csv
efficient_frontier.csv
```

Reports are stored under:

```text
reports/performance/
```

---

# 16. Version

Current API version:

```text
1.0.0
```

