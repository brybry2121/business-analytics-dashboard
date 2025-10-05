import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('../campaign.db')
df = pd.read_sql_query('SELECT * FROM sales LIMIT 5', conn)
print(df)
conn.close()