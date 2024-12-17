import os
import polars as pl
import logging
from datetime import datetime as dt

RUN_DATE = dt.strftime(dt.now(), "%Y-%m-%d")

os.makedirs(".log", exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s", 
    handlers=[logging.FileHandler(f".log/parquetize-{RUN_DATE}.log")]
)

def save_file_as_parquet(f: str):

    logging.info(f"Reading {f}")
    tableName = f.replace(".csv", "")

    try:

        table = pl.read_csv(f"data/csv/{tableName}.csv")
        table.write_parquet(f"data/parquet/{tableName}.parquet")

        logging.info(f"Wrote {f} successfully")

    except Exception as e:
        logging.error(f"Encountered error when writing {f}: {e}")

def main():
        csvs = os.listdir("data/csv/")
        [save_file_as_parquet(f) for f in csvs]

if __name__ == "__main__":
    main()
