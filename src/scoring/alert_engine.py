import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM alerts")

cursor.execute("""
SELECT
    project_name,
    priority,
    reason
FROM high_opportunities
""")

opportunities = cursor.fetchall()

for project_name, priority, reason in opportunities:

    alert_message = (
        f"{priority}: {project_name} | {reason}"
    )

    cursor.execute("""
    INSERT INTO alerts
    (
        project_name,
        priority,
        alert_message
    )
    VALUES (?, ?, ?)
    """,
    (
        project_name,
        priority,
        alert_message
    ))

conn.commit()
conn.close()

print("Alerts generated successfully!")