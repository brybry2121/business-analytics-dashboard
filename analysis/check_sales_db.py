import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('campaign.db')  # Adjust path if needed

# Load data
df = pd.read_sql_query('SELECT * FROM sales LIMIT 5', conn)
print("\n=== Sample: first 5 rows from sales table ===")
print(df)

# Show column info
print("\n=== Data Types in sales table ===")
print(df.dtypes)

# Show row count in sales table
count_df = pd.read_sql_query('SELECT COUNT(*) as row_count FROM sales', conn)
print("\n=== Total rows in sales table ===")
print(count_df)

# Describe numeric columns
describe_df = pd.read_sql_query('SELECT * FROM sales', conn)
print("\n=== Summary stats ===")
print(describe_df.describe())

conn.close()