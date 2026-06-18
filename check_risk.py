import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM risk_intelligence"
)

print(
    "Risk records:",
    cursor.fetchone()[0]
)

conn.close()