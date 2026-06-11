import sqlite3

from opportunity_score import calculate_score

# Connect to database
conn = sqlite3.connect("database/news.db")

cursor = conn.cursor()

# Read project data
cursor.execute("""
SELECT
    project_id,
    project_type,
    budget,
    agency
FROM projects
""")

projects = cursor.fetchall()

# Calculate scores
for project in projects:

    project_id = project[0]
    project_type = project[1]
    budget = project[2]
    agency = project[3]

    score = calculate_score(
        project_type,
        budget,
        agency
    )

    cursor.execute("""
    UPDATE projects
    SET opportunity_score = ?
    WHERE project_id = ?
    """,
    (
        score,
        project_id
    ))

# Save changes
conn.commit()

conn.close()

print("Opportunity scores updated successfully!")