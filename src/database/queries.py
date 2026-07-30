"""
                        queries.py

                        Part of Portfolio Analytics Platform.
                        
SQL queries used by the Portfolio Analytics Platform.

"""

# ==========================================================
# CREATE TABLES
# ==========================================================

CREATE_PRICES_TABLE = """
CREATE TABLE IF NOT EXISTS prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    date TEXT NOT NULL,
    open REAL NOT NULL,
    high REAL NOT NULL,
    low REAL NOT NULL,
    close REAL NOT NULL,
    volume INTEGER NOT NULL,
    UNIQUE(ticker, date)
);
"""

CREATE_PREDICTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    date TEXT NOT NULL,
    prediction REAL NOT NULL,
    confidence REAL,
    model TEXT NOT NULL
);
"""

CREATE_PORTFOLIO_TABLE = """
CREATE TABLE IF NOT EXISTS portfolio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL,
    weight REAL NOT NULL
);
"""

CREATE_BACKTEST_TABLE = """
CREATE TABLE IF NOT EXISTS backtests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    strategy TEXT NOT NULL,
    annual_return REAL,
    sharpe REAL,
    max_drawdown REAL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
"""

# ==========================================================
# PRICE QUERIES
# ==========================================================

INSERT_PRICE = """
INSERT OR REPLACE INTO prices (
    ticker,
    date,
    open,
    high,
    low,
    close,
    volume
)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""

SELECT_PRICE_HISTORY = """
SELECT
    date,
    open,
    high,
    low,
    close,
    volume
FROM prices
WHERE ticker = ?
ORDER BY date;
"""

SELECT_LATEST_PRICE = """
SELECT *
FROM prices
WHERE ticker = ?
ORDER BY date DESC
LIMIT 1;
"""

DELETE_PRICE_HISTORY = """
DELETE FROM prices
WHERE ticker = ?;
"""

# ==========================================================
# PREDICTION QUERIES
# ==========================================================

INSERT_PREDICTION = """
INSERT INTO predictions (
    ticker,
    date,
    prediction,
    confidence,
    model
)
VALUES (?, ?, ?, ?, ?);
"""

SELECT_PREDICTIONS = """
SELECT *
FROM predictions
WHERE ticker = ?
ORDER BY date;
"""

# ==========================================================
# PORTFOLIO QUERIES
# ==========================================================

INSERT_PORTFOLIO = """
INSERT INTO portfolio (
    ticker,
    weight
)
VALUES (?, ?);
"""

SELECT_PORTFOLIO = """
SELECT *
FROM portfolio;
"""

DELETE_PORTFOLIO = """
DELETE FROM portfolio;
"""

# ==========================================================
# BACKTEST QUERIES
# ==========================================================

INSERT_BACKTEST = """
INSERT INTO backtests (
    strategy,
    annual_return,
    sharpe,
    max_drawdown
)
VALUES (?, ?, ?, ?);
"""

SELECT_BACKTESTS = """
SELECT *
FROM backtests
ORDER BY created_at DESC;
"""