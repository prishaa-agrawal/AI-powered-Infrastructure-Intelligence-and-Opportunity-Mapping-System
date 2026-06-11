import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
project_name,
project_type,
budget,
opportunity_score
FROM projects
ORDER BY opportunity_score DESC
LIMIT 10
""")

rows = cursor.fetchall()

for row in rows:
    print(row)
    print("-" * 80)

conn.close()