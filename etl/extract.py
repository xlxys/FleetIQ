import pandas as pd
import logging


def extract_data(filepath: str) -> pd.DataFrame:
    """
    Extract data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Extracted data as a DataFrame.
    """
    try:
        df = pd.read_csv(filepath)
        logging.info(f"Extracted {len(df)} rows from {filepath}")
        return df
    except Exception as e:
        logging.error(f"Error extracting data: {e}")
        raise