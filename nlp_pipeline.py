import re

clinical_notes = [
    "Patient has heart attack and high blood pressure",
    "History of myocardial infarction and hypertension",
    "Signs of diabetes mellitus"
]

mapping = {
    "heart attack": "myocardial infarction",
    "high blood pressure": "hypertension"
}

def normalize(text):
    text = text.lower()
    for k, v in mapping.items():
        text = re.sub(k, v, text)
    return text

for note in clinical_notes:
    print("Original:", note)
    print("Normalized:", normalize(note))
    print("---")
