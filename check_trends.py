import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM trend_intelligence"
)

print(
    "Total trends:",
    cursor.fetchone()[0]
)

conn.close()