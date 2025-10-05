import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Query total units sold by category
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
conn.close()

# Pie chart
plt.figure(figsize=(8,8))
plt.pie(df['total_units_sold'], labels=df['category'], autopct='%1.1f%%', startangle=140)
plt.title('Total Units Sold by Product Category')
plt.axis('equal')  # Ensures pie is a circle
plt.show()