# ads_ecom


Ads + Ecommerce Analytics Engineering Pipeline
A full end‑to‑end analytics engineering project combining:

✅ Data ingestion (Bronze)

✅ Data cleaning & modeling (Silver)

✅ Business logic & attribution (Gold)

✅ BigQuery warehouse

✅ Looker Studio dashboards

✅ Advanced Add‑Ons:

Quantum Random Walk Attribution

Graph‑Based Multi‑Path Attribution

Budget Optimization (Quantum‑Inspired + Classical)

Portfolio‑Style Ad Spend Optimizer

ML Experiments (LTV, Churn, Uplift)

This project is designed to demonstrate real‑world data engineering, analytics engineering, and research‑grade modeling for interviews.


🏗 Architecture Overview

            ┌──────────────────────┐
            │      Ingestion       │
            │      (Bronze)        │
            └─────────┬────────────┘
                      │
                      ▼
            ┌──────────────────────┐
            │   Cleaning & Models  │
            │      (Silver)        │
            └─────────┬────────────┘
                      │
                      ▼
            ┌──────────────────────┐
            │   Business Logic     │
            │      (Gold)          │
            └─────────┬────────────┘
                      │
                      ▼
            ┌──────────────────────┐
            │  Dashboards (Looker) │
            └─────────┬────────────┘
                      │
                      ▼
            ┌──────────────────────────────┐
            │           Add‑Ons            │
            │ Quantum RW Attribution       │
            │ Graph‑Based Attribution
            Portfolio Optimizer          │
            │ ML Experiments  

Bronze Layer — Raw Ingestion
Scripts under ingestion/ fetch:

Ads spend data

Ecommerce orders

Web analytics sessions

Stored in data_raw/ and optionally uploaded to BigQuery.

🥈 Silver Layer — Cleaning & Standardization
SQL + Python transformations:

Normalize column names

Convert timestamps

Validate schema

Remove duplicates

Add metadata (ingested_at, processed_at)

Stored in data_clean/ and in BigQuery as *_silver tables.

🥇 Gold Layer — Business Logic
BigQuery SQL models for:

Customer journeys

Multi‑touch attribution

ROAS, CAC, LTV

Funnel metrics

Channel performance

Stored in BigQuery as *_gold tables.

🔮 Add‑Ons (Advanced Analytics)
✅ Quantum Random Walk Attribution
Models customer journeys as a graph and uses quantum‑inspired random walks to compute:

Path probabilities

Channel influence

Multi‑touch attribution weights

✅ Graph‑Based Probabilistic Attribution
Includes:

Markov chain attribution

Removal effect

Shapley value attribution

✅ Budget Optimization
Two solvers:

Quantum‑inspired QAOA optimizer

Classical linear programming optimizer
