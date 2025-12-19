from ingestion.fetch_ads import fetch_ads
from ingestion.fetch_ecommerce import fetch_ecommerce
from ingestion.fetch_web_analytics import fetch_web_analytics

def run_ingestion():
    steps = [
        ("ads", fetch_ads),
        ("ecommerce", fetch_ecommerce),
        ("web_analytics", fetch_web_analytics),
    ]

    for name, fn in steps:
        print(f"\n--- Running {name} ingestion ---")
        fn()

if __name__ == "__main__":
    run_ingestion()
