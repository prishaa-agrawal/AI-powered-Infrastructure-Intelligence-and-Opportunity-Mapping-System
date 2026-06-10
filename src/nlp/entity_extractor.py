import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):

    organizations = []
    locations = []

    doc = nlp(text)

    for ent in doc.ents:

        if ent.label_ == "ORG":
            organizations.append(ent.text)

        elif ent.label_ in ["GPE", "LOC"]:
            locations.append(ent.text)

    return organizations, locations