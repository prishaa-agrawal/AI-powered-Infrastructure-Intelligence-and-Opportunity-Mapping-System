import re

def extract_budget(text):
    """
    Extract budget values such as:
    ₹447.58 Crore
    ₹50 Lakh
    500 Million
    2 Billion
    """

    pattern = r'₹?\s?\d+(?:,\d+)*(?:\.\d+)?\s*(?:crore|cr|lakh|lakhs|million|billion)'

    matches = re.findall(pattern, text, flags=re.IGNORECASE)

    return matches


# Test code (runs only when this file is executed directly)
if __name__ == "__main__":

    text1 = "Indian Railways Approves ₹447.58 Crore Electric Traction Upgrade Projects"

    text2 = "ADB approves 500 Million loan for Green Infrastructure Projects"

    print(extract_budget(text1))
    print(extract_budget(text2))