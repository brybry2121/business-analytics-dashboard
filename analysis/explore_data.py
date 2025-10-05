import sqlite3
import pandas as pd

conn = sqlite3.connect('../campaign.db')

# Total units sold per product
query = """
SELECT product, SUM(units_sold) AS total_units_sold
FROM sales
GROUP BY product;
"""
df = pd.read_sql_query(query, conn)
print("Total units sold per product:")
print(df)

# Promotion impact analysis
query2 = """
SELECT product, promotion, AVG(units_sold) AS avg_units_sold
FROM sales
GROUP BY product, promotion;
"""
promo_df = pd.read_sql_query(query2, conn)
print("\nPromotion impact (average units sold):")
print(promo_df)

conn.close()