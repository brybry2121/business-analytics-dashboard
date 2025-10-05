import sqlite3
import pandas as pd

conn = sqlite3.connect('campaign.db')

# Example: Join fact_sales with product and promotion
query = """
SELECT 
    fs.date,
    dp.product_name,
    fs.units_sold,
    fs.price,
    dp.category,
    dp.product_id,
    pr.promotion_name,
    pr.discount_percent
FROM fact_sales fs
JOIN dim_product dp ON fs.product_id = dp.product_id
JOIN dim_promotion pr ON fs.promotion_id = pr.promotion_id
ORDER BY fs.date
LIMIT 10
"""
df = pd.read_sql_query(query, conn)
print(df)

conn.close()