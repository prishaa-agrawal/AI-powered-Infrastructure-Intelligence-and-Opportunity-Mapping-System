def calculate_score(project_type, budget, agency):

    score = 0

    # Budget Score
    if budget:

        budget = budget.lower()

        if "lakh crore" in budget:
            score += 50

        elif "crore" in budget:
            score += 40

        elif "million" in budget:
            score += 30

        elif "lakh" in budget:
            score += 20

    # Project Type Score
    if project_type == "Railway":
        score += 25

    elif project_type == "Tunnel":
        score += 20

    elif project_type == "Infrastructure":
        score += 15

    elif project_type == "Road":
        score += 15

    # Agency Score
    if agency:

        agency = agency.lower()

        if "world bank" in agency:
            score += 20

        elif "adb" in agency:
            score += 18

        elif "indian railways" in agency:
            score += 15

        elif "l&t" in agency:
            score += 12

        elif "larsen & toubro" in agency:
            score += 12

        elif "ntpc" in agency:
            score += 10

    return min(score, 100)


if __name__ == "__main__":

    score = calculate_score(
        "Railway",
        "₹447.58 Crore",
        "Indian Railways"
    )

    print("Opportunity Score:", score)