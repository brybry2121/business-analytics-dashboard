import os
import pandas as pd
import json

STAGING_DIR = './staging'

for filename in os.listdir(STAGING_DIR):
    file_path = os.path.join(STAGING_DIR, filename)
    print(f"\n--- Sample from {filename} ---")
    try:
        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
            print(df.head())
        elif filename.endswith('.json'):
            with open(file_path, 'r') as f:
                data = json.load(f)
            # Print first item, if it's a list
            if isinstance(data, list):
                print(data[:2])
            else:
                print(data)
        elif filename.endswith('.xlsx'):
            df = pd.read_excel(file_path)
            print(df.head())
        else:
            print("Unsupported file type.")
    except Exception as e:
        print(f"Error reading {filename}: {e}")