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

con = duckdb.connect("data/db/js-tennis.duckdb")

con.sql("drop table if exists raw_matches;")

con.sql("create schema if not exists raw;")

con.sql("""
    create or replace table raw.matches as (
        select * 
        from 'data/parquet/charting-m-matches.parquet');
""")
