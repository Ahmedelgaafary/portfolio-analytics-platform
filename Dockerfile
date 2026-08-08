# =======================================================
# Dockerfile for the project Portfolio Analytics Platform
# =======================================================

FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY tests ./tests
COPY notebooks ./notebooks
COPY data ./data
COPY models ./models
COPY reports ./reports
COPY docs ./docs
COPY pyproject.toml .
COPY README.md .

RUN mkdir -p \
    data/raw \
    data/processed \
    data/cache \
    data/exports \
    models/xgboost \
    models/random_forest \
    reports/figures \
    reports/performance \
    logs

CMD ["python", "-m", "src.app"]