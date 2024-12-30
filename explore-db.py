import duckdb

con = duckdb.connect("data/db/match_tracking.duckdb")

results = con.sql("select * from raw.shot_direction limit 1;")

# con.sql("drop table if exists main.cleansed_matches")

# results = con.sql("show all tables")

print(results)