# ads_ecom

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
