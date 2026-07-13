from transformers import pipeline
from app.config import MODEL_NAMES

classifier = None

def extract_event_themes(description: str, candidate_labels=None):
    global classifier
    if classifier is None:
        classifier = pipeline("zero-shot-classification", model=MODEL_NAMES["event_analysis"])
        
    if candidate_labels is None:
        candidate_labels = ["AI", "healthcare", "blockchain", "education", "sustainability"]
    result = classifier(description, candidate_labels)
    return result["labels"][:3] # top 3 themes
