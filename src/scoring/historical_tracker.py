import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

# Total projects
cursor.execute("SELECT COUNT(*) FROM projects")
total_projects = cursor.fetchone()[0]

# High opportunities
cursor.execute("SELECT COUNT(*) FROM high_opportunities")
high_opportunities = cursor.fetchone()[0]

# Average score
cursor.execute("""
SELECT AVG(opportunity_score)
FROM projects
""")
avg_score = cursor.fetchone()[0]

# Total agencies
cursor.execute("""
SELECT COUNT(DISTINCT agency)
FROM projects
""")
total_agencies = cursor.fetchone()[0]

cursor.execute("""
INSERT INTO daily_metrics
(
    total_projects,
    high_opportunities,
    avg_score,
    total_agencies
)
VALUES (?, ?, ?, ?)
""",
(
    total_projects,
    high_opportunities,
    round(avg_score, 2),
    total_agencies
))

conn.commit()
conn.close()

print("Historical metrics saved successfully!")