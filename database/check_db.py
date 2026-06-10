import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM news_articles")

count = cursor.fetchone()[0]

print("Total Articles:", count)

conn.close()