import sqlite3
import pandas as pd

# Load your sales CSV
df = pd.read_csv('staging/raw_sales_data.csv')

# Connect to DB
conn = sqlite3.connect('campaign.db')

# Write DataFrame to SQLite table
df.to_sql('sales', conn, if_exists='replace', index=False)
print("Sales table created and data imported.")

conn.close()