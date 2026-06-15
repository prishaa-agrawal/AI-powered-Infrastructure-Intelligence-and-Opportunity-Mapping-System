import sqlite3

from entity_extractor import extract_entities
from budget_extractor import extract_budget
from project_type_extractor import extract_project_type
from agency_extractor import extract_agency

# Connect to database
conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

# Clear old records to avoid duplicates
cursor.execute("DELETE FROM projects")

# Read all article titles
cursor.execute("SELECT title FROM news_articles")
articles = cursor.fetchall()

for article in articles:

    title = article[0]

    # Extract information
    orgs, locations = extract_entities(title)
    budgets = extract_budget(title)
    project_type = extract_project_type(title)
    agencies = extract_agency(title)


    # Use agency extractor if it finds something,
    # otherwise fall back to spaCy organizations
    if agencies:
        organization = ", ".join(agencies)
    else:
        organization = ", ".join(orgs)

    location = ", ".join(locations)
    budget = ", ".join(budgets)

    # Store in projects table
    cursor.execute("""
    INSERT INTO projects
    (
        project_name,
        project_type,
        budget,
        location,
        agency,
        status,
        summary,
        opportunity_score
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        title,
        project_type,
        budget,
        location,
        organization,
        "",
        "",
        0
    ))

# Save changes
conn.commit()
conn.close()

print("\nProjects stored successfully!")