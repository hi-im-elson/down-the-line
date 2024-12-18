rm data/db/match_tracking.duckdb
python3 scripts/write-csv-to-parquet.py
python3 scripts/populate-duckdb.py
cd etl
dbt run
