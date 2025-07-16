import duckdb
con = duckdb.connect("keywords.duckdb")

# Create a table with a placeholder value (can be updated later)
con.execute("""
    CREATE OR REPLACE TABLE parameters AS 
    SELECT 'Tableau' AS keyword, 'Boston' AS location;
""")
con.close()