def extract_agency(text):

    agencies = [
        "ADB",
        "Asian Development Bank",
        "World Bank",
        "NHAI",
        "MoRTH",
        "Indian Railways",
        "NTPC",
        "GAIL",
        "NPCIL",
        "DMRC",
        "PM Modi"
        "PM India",
        "L&T",
        "Larsen & Toubro"
    ]
    

    found = []

    for agency in agencies:
        if agency.lower() in text.lower():
            found.append(agency)

    return found


# Testing
if __name__ == "__main__":

    text = "India Secures $500 Million ADB Loan for Green Infrastructure Projects"

    print(extract_agency(text))