import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect and load data
conn = sqlite3.connect('campaign.db')
df = pd.read_sql_query("SELECT * FROM fact_sales", conn)
products = pd.read_sql_query("SELECT * FROM dim_product", conn)
conn.close()

# Sidebar: Filter by category
category = st.sidebar.selectbox("Select category", products['category'].unique())
filtered = df.merge(products, left_on='product_id', right_on='product_id')
filtered = filtered[filtered['category'] == category]

# Show table
st.write(f"Sales data for category: {category}", filtered)

# Pie chart
fig, ax = plt.subplots()
ax.pie(filtered.groupby('product_name')['units_sold'].sum(), labels=filtered['product_name'].unique(), autopct='%1.1f%%')
st.pyplot(fig)

# Download button
csv = filtered.to_csv(index=False)
st.download_button("Download filtered data as CSV", csv, "filtered_data.csv")