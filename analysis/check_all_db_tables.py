import sqlite3
import pandas as pd

conn = sqlite3.connect('campaign.db')
tables = ['sales', 'product', 'promotion', 'customer']

for table in tables:
    print(f"\n=== {table.upper()} TABLE: Sample ===")
    df = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 5", conn)
    print(df)
    
    print(f"\n=== {table.upper()} TABLE: Columns & Types ===")
    print(df.dtypes)
    
    count_df = pd.read_sql_query(f"SELECT COUNT(*) as row_count FROM {table}", conn)
    print(f"\nTotal rows in {table}: {count_df.iloc[0,0]}")

conn.close()