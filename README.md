# Readme
# Portfolio Analytics Platform

A modular Python platform for portfolio analytics, portfolio optimization, machine learning, risk analysis, and historical backtesting.

## Overview

The Portfolio Analytics Platform provides an end-to-end workflow for quantitative portfolio analysis:

```text
Market Data
     ↓
Data Processing
     ↓
Database
     ↓
Statistics
     ↓
Portfolio Optimization
     ↓
Machine Learning
     ↓
Risk Analytics
     ↓
Backtesting
     ↓
Visualization & Reports
```

The project is designed as a modular quantitative-finance application rather than a single notebook.

## Main Features

### Market Data

* Historical market data downloading
* Data preprocessing
* Local caching
* Data loading

### Database

* Database connection management
* Database schema
* Data models
* Repository layer
* Reusable queries

### Portfolio Statistics

* Simple returns
* Covariance matrix
* Correlation matrix
* Expected portfolio return
* Portfolio volatility

### Portfolio Optimization

The platform supports:

* Equal-weight portfolio
* Minimum-variance portfolio
* Maximum-Sharpe portfolio
* Markowitz optimization
* Efficient frontier generation

### Risk Analytics

* Sharpe ratio
* Sortino ratio
* Maximum drawdown
* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Annualized volatility
* Cumulative return

### Machine Learning

The ML layer provides:

* Feature engineering
* Data preprocessing
* Model training
* Prediction
* Model evaluation
* Random Forest
* XGBoost

### Backtesting

The backtesting engine provides:

* Historical portfolio simulation
* Portfolio return calculation
* Portfolio rebalancing
* Benchmark comparison
* Performance analysis

### Visualization

The platform provides:

* Price-history plots
* Cumulative-return plots
* Efficient-frontier visualization
* Performance reports
* Portfolio allocation display

## Project Structure

```text
portfolio-analytics-platform/
│
├── src/
│   ├── app.py
│   ├── config.py
│   │
│   ├── data_processing/
│   │   ├── __init__.py
│   │   ├── downloader.py
│   │   ├── preprocessing.py
│   │   ├── cache.py
│   │   └── loaders.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   ├── schema.py
│   │   ├── models.py
│   │   ├── repository.py
│   │   └── queries.py
│   │
│   ├── statistics/
│   │   ├── __init__.py
│   │   ├── returns.py
│   │   ├── covariance.py
│   │   ├── correlation.py
│   │   └── portfolio_statistics.py
│   │
│   ├── optimization/
│   │   ├── __init__.py
│   │   ├── constraints.py
│   │   ├── objective_functions.py
│   │   ├── markowitz.py
│   │   ├── efficient_frontier.py
│   │   ├── minimum_variance.py
│   │   ├── maximum_sharpe.py
│   │   ├── equal_weight.py
│   │   └── optimizer_factory.py
│   │
│   ├── ml/
│   │   ├── __init__.py
│   │   ├── feature_engineering.py
│   │   ├── preprocessing.py
│   │   ├── train.py
│   │   ├── predict.py
│   │   ├── evaluation.py
│   │   └── models/
│   │       ├── __init__.py
│   │       ├── xgboost_model.py
│   │       └── random_forest_model.py
│   │
│   ├── analytics/
│   │   ├── __init__.py
│   │   ├── performance.py
│   │   ├── sharpe.py
│   │   ├── sortino.py
│   │   ├── drawdown.py
│   │   ├── var.py
│   │   └── cvar.py
│   │
│   ├── backtesting/
│   │   ├── __init__.py
│   │   ├── engine.py
│   │   ├── portfolio.py
│   │   ├── rebalancing.py
│   │   └── benchmark.py
│   │
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── plots.py
│   │   ├── dashboard.py
│   │   └── reports.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       ├── validators.py
│       ├── export.py
│       └── helpers.py
│
├── tests/
├── notebooks/
├── data/
├── models/
├── reports/
├── docs/
│
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
└── LICENSE
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ahmedelgaafary/portfolio-analytics-platform.git
```

```bash
cd portfolio-analytics-platform
```

### 2. Create a virtual environment

Windows:

```bash
py -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
py -m pip install -r requirements.txt
```

### 4. Run tests

```bash
py -m pytest -v
```

## Running the Application

From the project root:

```bash
python -m src.app
```

The application downloads market data, calculates portfolio statistics, optimizes the portfolio, generates an efficient frontier, runs the backtest, calculates risk metrics, and exports results.

## Outputs

Generated outputs include:

```text
data/
└── exports/
    ├── portfolio_weights.csv
    ├── performance_metrics.csv
    └── efficient_frontier.csv

reports/
└── performance/
    └── portfolio_report.txt
```

## Example Portfolio Metrics

The platform calculates metrics such as:

```text
Annual Return
Annual Volatility
Cumulative Return
Sharpe Ratio
Sortino Ratio
Maximum Drawdown
Value at Risk
Conditional Value at Risk
```

## Machine Learning

The ML pipeline supports supervised prediction using engineered market features.

Current models include:

* XGBoost
* Random Forest

The pipeline is organized as:

```text
Feature Engineering
        ↓
Preprocessing
        ↓
Training
        ↓
Prediction
        ↓
Evaluation
```

## Backtesting

The backtesting layer evaluates portfolio strategies against historical market data.

```text
Historical Prices
       ↓
Asset Returns
       ↓
Portfolio Weights
       ↓
Portfolio Returns
       ↓
Performance Metrics
```

## Docker

Build the image:

```bash
docker build -t portfolio-analytics-platform .
```

Run:

```bash
docker run --rm portfolio-analytics-platform
```

Or use Docker Compose:

```bash
docker compose up --build
```

## Testing

Run the complete test suite:

```bash
py -m pytest -v
```

The tests cover:

* Data processing
* Database
* Statistics
* Optimization
* Machine learning
* Backtesting
* Integration
* Utilities

## Architecture

The system follows a modular architecture where each major quantitative-finance responsibility is separated into its own package.

See:

```text
docs/architecture.md
```

for the detailed architecture.

## Version

Current version:

```text
1.0.0
```

## License

This project is licensed under the MIT License.

See `LICENSE` for details.

