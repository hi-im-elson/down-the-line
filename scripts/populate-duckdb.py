import os
import duckdb
import logging
from datetime import datetime as dt

RUN_DATE = dt.strftime(dt.now(), "%Y-%m-%d")

os.makedirs(".log", exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s", 
    handlers=[logging.FileHandler(f".log/etl-duckdb-{RUN_DATE}.log")]
)

con = duckdb.connect("data/db/match_tracking.duckdb")

con.sql("create schema if not exists raw;")
con.sql("create schema if not exists stg;")

tableMapping = {
    "matches": "charting-m-matches",
    "shot_direction": "charting-m-stats-ShotDirOutcomes",
}

def create_table_from_parquet(table, parquet):

    logging.info(f"Reading {parquet}.parquet")

    try:

        con.sql(f"""
            create or replace table raw.{table} as (
                select * 
                from 'data/parquet/{parquet}.parquet');
        """)

        logging.info(f"Sucessfully created {table}")

    except Exception as e:

        logging.error(f"Error when trying to create table {table}")

def main():
    for table, parquet in tableMapping.items():
        create_table_from_parquet(table, parquet)

if __name__ == "__main__":
    main()
