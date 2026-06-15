import sqlite3

from entity_extractor import extract_entities
from budget_extractor import extract_budget
from project_type_extractor import extract_project_type

conn = sqlite3.connect("database/news.db")
cursor = conn.cursor()

cursor.execute("SELECT title FROM news_articles LIMIT 5")

articles = cursor.fetchall()

for article in articles:

    title = article[0]

    orgs, locations = extract_entities(title)
    budgets = extract_budget(title)
    project_type = extract_project_type(title)

    print("\nTitle:", title)
    print("Organization:", orgs)
    print("Location:", locations)
    print("Budget:", budgets)
    print("Project Type:", project_type)
    print("-" * 80)

conn.close()