import pandas as pd
import logging

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        # Remove missing values
        df = df.dropna()
        logging.info("Dropped NA values.")

        # Remove duplicates
        df = df.drop_duplicates()
        logging.info("Dropped duplicate rows.")

        # Convert data types
        df['start_time'] = pd.to_datetime(df['start_time'], errors='coerce')
        df['end_time'] = pd.to_datetime(df['end_time'], errors='coerce')

        # Filter out rows with invalid dates
        df = df[(df['start_time'] >= '2020-01-01') & (df['end_time'] <= '2023-12-31')]
        logging.info("Filtered rows based on date range.")

        # Calculate duration
        df['duration'] = (df['end_time'] - df['start_time']).dt.total_seconds() / 60 
        logging.info("Calculated duration in minutes.")

        # Drop rows with negative duration
        df = df[df['duration'] >= 0]
        logging.info("Dropped rows with negative duration.")

        logging.info(f"Transformed data, remaining {len(df)} rows.")
        return df
    except Exception as e:
        logging.error(f"Error during transformation: {e}")
        raise
