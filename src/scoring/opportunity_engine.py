import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

import sqlite3

from config import DATABASE_PATH

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

cursor.execute("""
SELECT
    project_name,
    agency,
    project_type,
    opportunity_score
FROM projects
WHERE opportunity_score >= 70
""")

projects = cursor.fetchall()

print(f"Found {len(projects)} high opportunity projects")
cursor.execute("DELETE FROM high_opportunities")

for project in projects:

    project_name = project[0]
    agency = project[1]
    project_type = project[2]
    score = project[3]

    reasons = []

    if score >= 85:
        priority = "Immediate Review"
        reasons.append("Very high opportunity score")

    elif score >= 70:
        priority = "High Potential"
        reasons.append("Strong opportunity score")

    else:
        priority = "Monitor"

    if agency:
        reasons.append("Recognized agency")

    if project_type:
        reasons.append(f"{project_type} sector opportunity")

    reason = ", ".join(reasons)
    cursor.execute("""
    INSERT INTO high_opportunities
    (
        project_name,
        agency,
        project_type,
        score,
        priority,
        reason
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    
    (
        project_name,
        agency,
        project_type,
        score,
        priority,
        reason
    ))

    print("\n" + "=" * 60)
    print("Project:", project_name)
    print("Priority:", priority)
    print("Reason:", reason)

conn.commit()
conn.close()

print("\nHigh opportunities stored successfully!")