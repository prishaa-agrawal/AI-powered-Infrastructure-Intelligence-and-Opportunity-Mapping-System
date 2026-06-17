import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM agency_intelligence")

print("Total agencies:", cursor.fetchone()[0])

conn.close()