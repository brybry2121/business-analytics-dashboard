import sqlite3
import pandas as pd

conn = sqlite3.connect('campaign.db')

# Product dimension
df_product = pd.read_csv('ods/product_data_ods.csv')
df_product.to_sql('dim_product', conn, if_exists='replace', index=False)

# Customer dimension
df_customer = pd.read_csv('ods/customers_ods.csv')
df_customer.to_sql('dim_customer', conn, if_exists='replace', index=False)

# Promotion dimension
df_promotion = pd.read_csv('ods/promotions_ods.csv')
df_promotion.to_sql('dim_promotion', conn, if_exists='replace', index=False)

conn.close()
print("Dimension tables populated.")