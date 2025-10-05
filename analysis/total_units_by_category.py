import sqlite3
import pandas as pd

conn = sqlite3.connect('campaign.db')
query = """
SELECT 
    dp.category, 
    SUM(fs.units_sold) as total_units_sold
FROM fact_sales fs
JOIN dim_product dp ON fs.product_id = dp.product_id
GROUP BY dp.category
ORDER BY total_units_sold DESC
"""
df = pd.read_sql_query(query, conn)
print(df)
conn.close()