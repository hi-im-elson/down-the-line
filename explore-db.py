import duckdb

con = duckdb.connect("data/db/js-tennis.duckdb")

results = con.sql("select * from matches limit 1;")

print(results)