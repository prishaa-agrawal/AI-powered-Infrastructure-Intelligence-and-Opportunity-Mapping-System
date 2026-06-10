def extract_project_type(text):

    text = text.lower()

    if "railway" in text or "rail" in text:
        return "Railway"

    elif "highway" in text or "road" in text:
        return "Road"

    elif "metro" in text:
        return "Metro"

    elif "water" in text:
        return "Water Supply"

    elif "tunnel" in text:
        return "Tunnel"

    elif "airport" in text:
        return "Airport"

    elif "smart city" in text:
        return "Smart City"

    elif "infrastructure" in text:
        return "Infrastructure"

    return "Unknown"