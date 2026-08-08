# Architecture
# Portfolio Analytics Platform — Architecture

## 1. System Overview

The Portfolio Analytics Platform is organized as a modular quantitative-finance system.

The architecture separates data processing, database operations, statistical analysis, optimization, machine learning, risk analytics, backtesting, visualization, and utility services.

```text
                         ┌─────────────────────┐
                         │       src/app.py    │
                         │   Application Layer  │
                         └──────────┬──────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
             ▼                      ▼                      ▼
      Data Processing          Database              Statistics
             │                      │                      │
             └──────────────────────┼──────────────────────┘
                                    │
                                    ▼
                            Optimization
                                    │
                   ┌────────────────┼────────────────┐
                   │                │                │
                   ▼                ▼                ▼
                  ML           Backtesting       Analytics
                   │                │                │
                   └────────────────┼────────────────┘
                                    │
                                    ▼
                           Visualization
                                    │
                                    ▼
                              Reports / Export
```

---

## 2. Application Layer

### `src/app.py`

`app.py` is the main entry point.

It coordinates the complete workflow:

```text
Configuration
     ↓
Market Data
     ↓
Returns
     ↓
Statistics
     ↓
Optimization
     ↓
Efficient Frontier
     ↓
Backtesting
     ↓
Risk Analytics
     ↓
Visualization
     ↓
Export
```

The application layer should coordinate modules rather than contain the mathematical implementation of each component.

---

## 3. Configuration Layer

### `src/config.py`

The configuration module contains application-wide settings.

Examples include:

* Database path
* Cache path
* Data directories
* Model directories
* Report directories
* Default tickers
* Risk-free rate
* Trading days
* Optimizer selection
* Efficient-frontier points
* Machine-learning parameters
* Logging configuration

This keeps configuration separate from business logic.

---

## 4. Data Processing Layer

Located in:

```text
src/data_processing/
```

Components:

```text
downloader.py
preprocessing.py
cache.py
loaders.py
```

### Downloader

Downloads historical market data.

### Preprocessing

Cleans and prepares market data for analysis.

### Cache

Stores downloaded data locally to reduce unnecessary downloads.

### Loaders

Loads raw or processed datasets for downstream modules.

The data flow is:

```text
External Market Data
        ↓
Downloader
        ↓
Cache
        ↓
Preprocessing
        ↓
Clean Data
```

---

## 5. Database Layer

Located in:

```text
src/database/
```

Components:

```text
connection.py
schema.py
models.py
repository.py
queries.py
```

### Connection

Manages the database connection.

### Schema

Defines database tables.

### Models

Represents application data structures.

### Repository

Provides an abstraction for storing and retrieving data.

### Queries

Contains reusable database queries.

The database layer separates persistence from analytical logic.

---

## 6. Statistics Layer

Located in:

```text
src/statistics/
```

Components:

```text
returns.py
covariance.py
correlation.py
portfolio_statistics.py
```

The statistics layer converts processed market data into quantitative portfolio inputs.

```text
Prices
  ↓
Returns
  ↓
Expected Returns
  ↓
Covariance Matrix
  ↓
Correlation Matrix
```

These outputs are consumed by the optimization layer.

---

## 7. Optimization Layer

Located in:

```text
src/optimization/
```

Components:

```text
constraints.py
objective_functions.py
markowitz.py
efficient_frontier.py
minimum_variance.py
maximum_sharpe.py
equal_weight.py
optimizer_factory.py
```

The optimization layer determines portfolio weights.

Supported strategies include:

### Equal Weight

Allocates approximately equal capital to each asset.

### Minimum Variance

Minimizes portfolio variance subject to portfolio constraints.

### Maximum Sharpe

Maximizes the risk-adjusted return.

### Markowitz

Implements mean-variance portfolio optimization.

### Efficient Frontier

Generates portfolios representing the risk-return trade-off.

The optimization flow is:

```text
Expected Returns
       +
Covariance Matrix
       +
Constraints
       ↓
Optimization
       ↓
Portfolio Weights
```

---

## 8. Machine Learning Layer

Located in:

```text
src/ml/
```

Components:

```text
feature_engineering.py
preprocessing.py
train.py
predict.py
evaluation.py
```

Models:

```text
src/ml/models/
├── xgboost_model.py
└── random_forest_model.py
```

The ML pipeline is:

```text
Market Data
     ↓
Feature Engineering
     ↓
Preprocessing
     ↓
Model Training
     ↓
Prediction
     ↓
Evaluation
```

The machine-learning layer can be used to generate predictive signals or features that can subsequently support portfolio decisions.

---

## 9. Analytics Layer

Located in:

```text
src/analytics/
```

Components:

```text
performance.py
sharpe.py
sortino.py
drawdown.py
var.py
cvar.py
```

The analytics layer evaluates portfolio performance and risk.

Metrics include:

* Annual return
* Annual volatility
* Cumulative return
* Sharpe ratio
* Sortino ratio
* Maximum drawdown
* VaR
* CVaR

The flow is:

```text
Portfolio Returns
       ↓
Performance Analytics
       ↓
Risk Metrics
       ↓
Performance Report
```

---

## 10. Backtesting Layer

Located in:

```text
src/backtesting/
```

Components:

```text
engine.py
portfolio.py
rebalancing.py
benchmark.py
```

The backtesting engine evaluates investment strategies against historical data.

```text
Historical Data
       ↓
Portfolio Strategy
       ↓
Portfolio Construction
       ↓
Rebalancing
       ↓
Portfolio Returns
       ↓
Performance Analysis
```

The benchmark component allows portfolio performance to be compared with a reference index or strategy.

---

## 11. Visualization Layer

Located in:

```text
src/visualization/
```

Components:

```text
plots.py
dashboard.py
reports.py
```

The visualization layer converts analytical results into human-readable outputs.

Examples:

* Price history
* Cumulative returns
* Efficient frontier
* Portfolio allocation
* Performance reports

The visualization layer consumes results from the analytical modules and does not perform core financial calculations.

---

## 12. Utilities Layer

Located in:

```text
src/utils/
```

Components:

```text
logger.py
validators.py
export.py
helpers.py
```

### Logger

Provides centralized application logging.

### Validators

Validates data, dates, tickers, and portfolio weights.

### Exporter

Exports analytical results to files.

### Helpers

Provides reusable helper functions such as:

* Directory creation
* Timestamp generation
* File checks
* Dictionary flattening

---

## 13. Testing Architecture

Tests are located in:

```text
tests/
```

```text
test_data.py
test_database.py
test_statistics.py
test_optimization.py
test_ml.py
test_backtesting.py
test_integration.py
test_utils.py
```

Testing is divided into:

### Unit Tests

Test individual components independently.

### Integration Tests

Test multiple components working together.

The main integration pipeline is:

```text
Prices
  ↓
Returns
  ↓
Statistics
  ↓
Optimization
  ↓
Backtesting
  ↓
Performance
```

---

## 14. Data Storage

The project separates data by purpose:

```text
data/
├── raw/
├── processed/
├── cache/
└── exports/
```

### Raw

Original downloaded market data.

### Processed

Cleaned and transformed data.

### Cache

Locally cached market data.

### Exports

Generated analytical results.

Models are stored separately:

```text
models/
├── xgboost/
└── random_forest/
```

Reports are stored separately:

```text
reports/
├── figures/
└── performance/
```

---

## 15. Dependency Flow

The main dependency direction is:

```text
Configuration
      ↓
Data Processing
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
```

Supporting layers:

```text
Database
Utils
Machine Learning
```

The goal is to keep individual modules focused on one responsibility.

---

## 16. Deployment

The application can be executed directly using Python:

```bash
python -m src.app
```

It can also be containerized using Docker:

```bash
docker build -t portfolio-analytics-platform .
```

Docker Compose provides a convenient execution environment:

```bash
docker compose up --build
```

---

## 17. Complete System Flow

The complete Version 1 workflow is:

```text
                    MARKET DATA
                         │
                         ▼
                 DATA PROCESSING
                         │
                         ▼
                    DATABASE
                         │
                         ▼
                    STATISTICS
                         │
                         ▼
                  OPTIMIZATION
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        PORTFOLIO                EFFICIENT
        WEIGHTS                  FRONTIER
              │                     │
              └──────────┬──────────┘
                         ▼
                    BACKTESTING
                         │
                         ▼
                     ANALYTICS
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        RISK METRICS          PERFORMANCE
              │                     │
              └──────────┬──────────┘
                         ▼
                  VISUALIZATION
                         │
                         ▼
                  REPORTS / EXPORT
```

This architecture provides the foundation for extending the platform with additional financial models, optimization strategies, machine-learning models, data sources, and reporting capabilities.

