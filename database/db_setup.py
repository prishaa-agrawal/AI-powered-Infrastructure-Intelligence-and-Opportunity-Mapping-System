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

cursor.execute("""
CREATE TABLE IF NOT EXISTS agency_intelligence (
    agency_id INTEGER PRIMARY KEY AUTOINCREMENT,
    agency_name TEXT,
    project_count INTEGER,
    avg_score REAL,
    influence_level TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS trend_intelligence (
    trend_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_type TEXT,
    project_count INTEGER,
    avg_score REAL,
    trend_level TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS daily_metrics (
    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_projects INTEGER,
    high_opportunities INTEGER,
    avg_score REAL,
    total_agencies INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS risk_intelligence (
    risk_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT,
    opportunity_score INTEGER,
    risk_score INTEGER,
    risk_level TEXT
)
""")
conn.commit()
conn.close()

print("Database created successfully!")