import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM agency_intelligence")

cursor.execute("""
SELECT
    agency,
    COUNT(*) as project_count,
    AVG(opportunity_score) as avg_score
FROM projects
WHERE agency IS NOT NULL
AND agency != ''
GROUP BY agency
""")

agencies = cursor.fetchall()

for agency, project_count, avg_score in agencies:

    if avg_score >= 70:
        influence = "High"

    elif avg_score >= 50:
        influence = "Medium"

    else:
        influence = "Low"

    cursor.execute("""
    INSERT INTO agency_intelligence
    (
        agency_name,
        project_count,
        avg_score,
        influence_level
    )
    VALUES (?, ?, ?, ?)
    """,
    (
        agency,
        project_count,
        round(avg_score, 2),
        influence
    ))

conn.commit()
conn.close()

print("Agency intelligence generated successfully!")