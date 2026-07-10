from transformers import pipeline

MODEL_NAME = "typeform/distilbert-base-uncased-mnli"

classifier = pipeline("zero-shot-classification", model=MODEL_NAME)

def extract_event_themes(description: str, candidate_labels=None):
    """Extract the top 3 themes from an event description using zero-shot classification."""
    if candidate_labels is None:
        candidate_labels = [
            "artificial intelligence", "healthcare", "blockchain",
            "education", "sustainability", "finance", "cybersecurity",
            "climate change", "robotics", "data science"
        ]
    result = classifier(description, candidate_labels)
    return result["labels"][:3]
