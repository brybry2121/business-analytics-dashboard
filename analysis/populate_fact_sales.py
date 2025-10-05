import sqlite3
import pandas as pd

conn = sqlite3.connect('campaign.db')

# Load sales data
df_sales = pd.read_csv('ods/sales_data_ods.csv')

# Map product name to product_id
product_map = pd.read_sql_query('SELECT product_id, product_name FROM dim_product', conn)
df_sales = df_sales.merge(product_map, left_on='product', right_on='product_name', how='left')

# Map promotion flag to promotion_id
# Assuming: 1 = first promotion, 0 = no promotion, or use your own mapping
promotion_map = pd.read_sql_query('SELECT promotion_id FROM dim_promotion', conn)
df_sales['promotion_id'] = df_sales['promotion'] + 1  # If promotion_id starts at 1, adjust as needed

# Prepare fact_sales DataFrame
fact_sales = df_sales[['date', 'product_id', 'units_sold', 'price', 'promotion_id']]

fact_sales.to_sql('fact_sales', conn, if_exists='replace', index=False)

conn.close()
print("Fact table populated.")