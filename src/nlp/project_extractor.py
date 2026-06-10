from entity_extractor import extract_entities
from budget_extractor import extract_budget

text = "Indian Railways Approves ₹447.58 Crore Electric Traction Upgrade Projects in South India"

orgs, locations = extract_entities(text)
budgets = extract_budget(text)

# Project Type Detection
project_type = "Unknown"

if "railway" in text.lower():
    project_type = "Railway"

elif "highway" in text.lower():
    project_type = "Road"

elif "metro" in text.lower():
    project_type = "Metro"

elif "water" in text.lower():
    project_type = "Water Supply"

print("Organization:", orgs)
print("Location:", locations)
print("Budget:", budgets)
print("Project Type:", project_type)