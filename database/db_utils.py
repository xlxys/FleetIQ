from sqlalchemy import create_engine
import yaml
import logging

def get_engine():
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    db = config["db"]
    url = f"postgresql://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"
    logging.info(f"Connecting to database at {url}")
    
    return create_engine(url)

def insert_dataframe(df, table_name):
    engine = get_engine()
    logging.info(f"Inserting data into {table_name} table")
    # Ensure the table exists
    with engine.connect() as conn:
        if not conn.dialect.has_table(conn, table_name):
            df.head(0).to_sql(table_name, con=engine, if_exists='replace', index=False)
    # Insert the data

    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    logging.info(f"Inserted {len(df)} records into {table_name} table")
    engine.dispose()
    