import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM trend_intelligence")

cursor.execute("""
SELECT
    project_type,
    COUNT(*) as project_count,
    AVG(opportunity_score) as avg_score
FROM projects
GROUP BY project_type
""")

trends = cursor.fetchall()

for project_type, project_count, avg_score in trends:

    if avg_score >= 70:
        trend_level = "Hot"

    elif avg_score >= 50:
        trend_level = "Growing"

    else:
        trend_level = "Stable"

    cursor.execute("""
    INSERT INTO trend_intelligence
    (
        project_type,
        project_count,
        avg_score,
        trend_level
    )
    VALUES (?, ?, ?, ?)
    """,
    (
        project_type,
        project_count,
        round(avg_score, 2),
        trend_level
    ))

conn.commit()
conn.close()

print("Trend intelligence generated successfully!")