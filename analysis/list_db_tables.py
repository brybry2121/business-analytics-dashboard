import sqlite3

conn = sqlite3.connect('campaign.db')
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print("Tables in database:", [t[0] for t in tables])
conn.close()