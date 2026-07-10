from transformers import pipeline, set_seed

MODEL_NAME = "gpt2"

generator = pipeline("text-generation", model=MODEL_NAME)
set_seed(42)

def generate_topics(event_themes, user_interests):
    """Generate creative conversation starters using GPT-2 text generation."""
    prompt = (
        f"I'm attending a networking event focused on {', '.join(event_themes)}.\n"
        f"I'm personally interested in {', '.join(user_interests)}.\n"
        f"What are three creative and engaging conversation starters I could use to break the ice?\n"
    )
    outputs = generator(prompt, max_length=120, num_return_sequences=1)
    raw_text = outputs[0]["generated_text"]

    # Strip off the prompt portion and extract only generated lines
    lines = raw_text.split("\n")[3:]
    suggestions = [s.strip("- ").strip() for s in lines if len(s.strip()) > 10]

    # Cap at 3 suggestions max
    return suggestions[:3]
