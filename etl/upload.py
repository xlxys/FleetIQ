import boto3
import logging

def upload_to_s3(file_path: str, bucket_name: str, s3_key: str):
    s3 = boto3.client("s3")
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        logging.info(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        logging.error(f"Upload failed: {e}")
        raise