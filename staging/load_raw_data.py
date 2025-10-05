import shutil
import os

SOURCE_DIR = '../data'
STAGING_DIR = './staging'

raw_files = [
    ('sales_data.csv', 'raw_sales_data.csv'),
    ('product_data.csv', 'raw_product_data.csv'),
    ('promotions.json', 'raw_promotions.json'),
    ('customers.xlsx', 'raw_customers.xlsx'),
]

os.makedirs(STAGING_DIR, exist_ok=True)

for src_name, dst_name in raw_files:
    src = os.path.join(SOURCE_DIR, src_name)
    dst = os.path.join(STAGING_DIR, dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {src_name} to staging as {dst_name}")
    else:
        print(f"Source file {src_name} not found in {SOURCE_DIR}")