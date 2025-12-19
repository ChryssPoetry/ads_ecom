# ads_ecom

ads_ecommerce_pipeline/
│
├── data_raw/              # raw ingested files (bronze layer)
├── data_clean/            # cleaned files (silver layer)
│
├── ingestion/
│   ├── fetch_ads.py
│   ├── fetch_ecommerce.py
│   ├── fetch_web_analytics.py
│
├── utils/
│   ├── quality_checks.py
│
└── main_ingest.py
