import logging
import yaml
import os

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)['etl']

# Logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename=config['log_path'],
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def main():
    try:
        logging.info("Starting ETL pipeline...")

        df_raw = extract_data(config['input_path'])
        df_clean = transform_data(df_raw)
        load_data(df_clean, config['output_path'])

        logging.info("ETL pipeline completed successfully.")
    except Exception as e:
        logging.error(f"ETL pipeline failed: {e}")

if __name__ == "__main__":
    main()
