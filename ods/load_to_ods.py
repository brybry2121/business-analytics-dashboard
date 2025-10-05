import pandas as pd
import json

# Sales and Product
sales = pd.read_csv('staging/raw_sales_data.csv')
product = pd.read_csv('staging/raw_product_data.csv')

# Promotions (JSON to DataFrame)
with open('staging/raw_promotions.json', 'r') as f:
    promo_data = json.load(f)
promotions = pd.DataFrame(promo_data)

# Customers (Excel to DataFrame)
customers = pd.read_excel('staging/raw_customers.xlsx')

# Example cleaning: remove duplicates
sales = sales.drop_duplicates()
product = product.drop_duplicates()
promotions = promotions.drop_duplicates()
customers = customers.drop_duplicates()

# Save cleaned data to ODS
sales.to_csv('ods/sales_data_ods.csv', index=False)
product.to_csv('ods/product_data_ods.csv', index=False)
promotions.to_csv('ods/promotions_ods.csv', index=False)
customers.to_csv('ods/customers_ods.csv', index=False)

print("ODS: All sources loaded and cleaned.")