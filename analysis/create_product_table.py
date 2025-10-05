import sqlite3
import pandas as pd

# Load product data
df = pd.read_csv('ods/product_data_ods.csv')

# Connect to DB
conn = sqlite3.connect('campaign.db')

# Write DataFrame to SQLite table
df.to_sql('product', conn, if_exists='replace', index=False)
print("Product table created and data imported.")

conn.close()