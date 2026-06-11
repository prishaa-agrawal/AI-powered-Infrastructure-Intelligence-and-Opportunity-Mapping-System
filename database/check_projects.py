import sqlite3

conn = sqlite3.connect("database/news.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
project_name,
project_type,
budget,
location,
agency
FROM projects
LIMIT 10
""")

rows = cursor.fetchall()

for row in rows:
    print(row)
    print("-" * 80)

conn.close()