import pandas as pd
from database.db_utils import insert_dataframe
import logging

def load_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Load the transformed DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_path (str): The path where the CSV file will be saved.
    """
    try:
        df.to_csv(output_path, index=False)
        logging.info(f"Saved cleaned data to {output_path}")
        insert_dataframe(df, table_name="fleet_data")
        logging.info(f"Inserted data into database table 'fleet_data'")
    except Exception as e:
        logging.error(f"Error saving data: {e}")
        raise