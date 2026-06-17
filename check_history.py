import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM daily_metrics")

print(
    "Historical snapshots:",
    cursor.fetchone()[0]
)

conn.close()