from src.intelligence.opportunity_briefs import (
    generate_brief
)

brief = generate_brief(
    project_name="Railway Electrification Project",
    agency="Indian Railways",
    score=85,
    risk_level="Low"
)

print(brief)