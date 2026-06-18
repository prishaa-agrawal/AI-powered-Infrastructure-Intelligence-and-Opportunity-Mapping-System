import sqlite3

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM risk_intelligence")

cursor.execute("""
SELECT
    project_name,
    project_type,
    agency,
    opportunity_score
FROM projects
WHERE opportunity_score > 0
""")

projects = cursor.fetchall()

for (
    project_name,
    project_type,
    agency,
    opportunity_score
) in projects:

    # Base Risk
    risk_score = (100 - opportunity_score) * 0.5

    # Agency Influence
    cursor.execute("""
    SELECT influence_level
    FROM agency_intelligence
    WHERE agency_name = ?
    """, (agency,))

    agency_result = cursor.fetchone()

    if agency_result:

        influence = agency_result[0]

        if influence == "Low":
            risk_score += 25

        elif influence == "Medium":
            risk_score += 10

    # Trend Intelligence
    cursor.execute("""
    SELECT trend_level
    FROM trend_intelligence
    WHERE project_type = ?
    """, (project_type,))

    trend_result = cursor.fetchone()

    if trend_result:

        trend = trend_result[0]

        if trend == "Stable":
            risk_score += 20

        elif trend == "Growing":
            risk_score += 10

    risk_score = min(
        100,
        round(risk_score)
    )

    if risk_score >= 70:
        risk_level = "High"

    elif risk_score >= 40:
        risk_level = "Medium"

    else:
        risk_level = "Low"

    cursor.execute("""
    INSERT INTO risk_intelligence
    (
        project_name,
        opportunity_score,
        risk_score,
        risk_level
    )
    VALUES (?, ?, ?, ?)
    """,
    (
        project_name,
        opportunity_score,
        risk_score,
        risk_level
    ))

conn.commit()
conn.close()

print("Risk intelligence generated successfully!")