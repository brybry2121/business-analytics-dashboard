import pandas as pd
import sqlite3

# Load CSV data
sales = pd.read_csv('../data/sales_data.csv')  # Adjust path if necessary

# Connect to SQLite and write table
conn = sqlite3.connect('../campaign.db')
sales.to_sql('sales', conn, if_exists='replace', index=False)
conn.close()