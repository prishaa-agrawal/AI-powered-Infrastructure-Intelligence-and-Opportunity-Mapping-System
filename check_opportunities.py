import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM high_opportunities")

print("Total opportunities:", cursor.fetchone()[0])

conn.close()