# check_risk_distribution.py

import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    risk_level,
    COUNT(*)
FROM risk_intelligence
GROUP BY risk_level
""")

for row in cursor.fetchall():
    print(row)

conn.close()