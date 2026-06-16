import sqlite3

conn = sqlite3.connect("database/news.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS news_articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    date TEXT,
    source TEXT,
    content TEXT,
    url TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT,
    project_type TEXT,
    budget TEXT,
    location TEXT,
    agency TEXT,
    status TEXT,
    summary TEXT,
    opportunity_score REAL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS high_opportunities (
    opportunity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT,
    agency TEXT,
    project_type TEXT,
    score INTEGER,
    priority TEXT,
    reason TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT,
    priority TEXT,
    alert_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()
conn.close()

print("Database created successfully!")