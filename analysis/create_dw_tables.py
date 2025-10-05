import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('campaign.db')
cur = conn.cursor()

# Create Dimension Tables
cur.execute("""
CREATE TABLE IF NOT EXISTS dim_product (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    region TEXT,
    signup_date TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS dim_promotion (
    promotion_id INTEGER PRIMARY KEY,
    promotion_name TEXT,
    start_date TEXT,
    end_date TEXT,
    discount_percent INTEGER
)
""")

# Create Fact Table
cur.execute("""
CREATE TABLE IF NOT EXISTS fact_sales (
    sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    product_id INTEGER,
    units_sold INTEGER,
    price REAL,
    promotion_id INTEGER,
    FOREIGN KEY(product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY(promotion_id) REFERENCES dim_promotion(promotion_id)
    -- Add customer_id INTEGER, FOREIGN KEY(customer_id) REFERENCES dim_customer(customer_id) if customer info is available per sale
)
""")

conn.commit()
conn.close()
print("All Data Warehouse tables created!")