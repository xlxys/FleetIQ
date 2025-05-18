import logging
import yaml
import os

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
from etl.upload import upload_to_s3

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename=config['etl']['log_path'],
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def main():
    try:
        logging.info("Starting ETL pipeline...")

        df_raw = extract_data(config['etl']['input_path'])
        df_clean = transform_data(df_raw)
        load_data(df_clean, config['etl']['output_path'])
        
        # Upload to S3
        bucket_name = config['s3']['bucket_name']
        output_file = config['etl']['output_path']
        s3_key = os.path.join(config['s3']['prefix'], os.path.basename(output_file))
        upload_to_s3(output_file, bucket_name, s3_key)
        
        
        logging.info("ETL pipeline completed successfully.")

    except Exception as e:
        logging.error(f"ETL pipeline failed: {e}")

if __name__ == "__main__":
    main()
