import sqlite3
import pandas as pd

# Load promotion data
df = pd.read_csv('ods/promotions_ods.csv')

# Connect to DB
conn = sqlite3.connect('campaign.db')

# Write DataFrame to SQLite table
df.to_sql('promotion', conn, if_exists='replace', index=False)
print("Promotion table created and data imported.")

conn.close()