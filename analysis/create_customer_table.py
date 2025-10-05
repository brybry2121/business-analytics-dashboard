import sqlite3
import pandas as pd

# Load customer data
df = pd.read_csv('ods/customers_ods.csv')

# Connect to DB
conn = sqlite3.connect('campaign.db')

# Write DataFrame to SQLite table
df.to_sql('customer', conn, if_exists='replace', index=False)
print("Customer table created and data imported.")

conn.close()