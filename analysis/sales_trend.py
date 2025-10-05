import sqlite3
import pandas as pd

conn = sqlite3.connect('campaign.db')
query = """
SELECT 
    fs.date,
    SUM(fs.units_sold) as total_units_sold
FROM fact_sales fs
GROUP BY fs.date
ORDER BY fs.date
"""
df = pd.read_sql_query(query, conn)
print(df)
conn.close()