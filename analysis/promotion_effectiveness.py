import sqlite3
import pandas as pd

conn = sqlite3.connect('campaign.db')
query = """
SELECT 
    pr.promotion_name,
    SUM(fs.units_sold) as total_units_sold,
    AVG(pr.discount_percent) as avg_discount
FROM fact_sales fs
JOIN dim_promotion pr ON fs.promotion_id = pr.promotion_id
GROUP BY pr.promotion_name
ORDER BY total_units_sold DESC
"""
df = pd.read_sql_query(query, conn)
print(df)
conn.close()