from app.services import topic_generator

def test_topic_generation_returns_suggestions():
    themes = ["AI", "healthcare"]
    interests = ["ethics", "automation"]
    suggestions = topic_generator.generate_topics(themes, interests)
    assert isinstance(suggestions, list)
    assert len(suggestions) > 0

def test_generate_strings():
    themes = ["AI"]
    interests = ["robots"]
    suggestions = topic_generator.generate_topics(themes, interests)
    for s in suggestions:
        assert isinstance(s, str)

def test_generate_non_empty_strings():
    themes = ["AI"]
    interests = ["robots"]
    suggestions = topic_generator.generate_topics(themes, interests)
    for s in suggestions:
        assert len(s.strip()) > 0
