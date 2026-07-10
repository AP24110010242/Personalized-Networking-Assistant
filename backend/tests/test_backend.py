import sys
import os
from pathlib import Path

# Add the backend directory to sys.path so imports work
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from app import app

client = TestClient(app)


# ─── Route Tests ───

def test_root_returns_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_generate_conversation_api():
    payload = {
        "description": "Sustainability in smart cities",
        "interests": ["green energy", "public transport"]
    }
    response = client.post("/generate-conversation", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "topics" in data
    assert "suggestions" in data

def test_fact_check_api():
    response = client.post("/fact-check", json={"query": "solar energy"})
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data

def test_invalid_request_returns_422():
    response = client.post("/generate-conversation", json={})
    assert response.status_code == 422


# ─── Event Analyzer Tests ───

def test_event_analysis_returns_labels():
    from event_analyzer import extract_event_themes
    result = extract_event_themes("AI in healthcare and diagnostics")
    assert isinstance(result, list)
    assert len(result) > 0


# ─── Fact Checker Tests ───

def test_fact_checker_returns_summary():
    from fact_checker import fact_check
    summary = fact_check("Artificial Intelligence")
    assert isinstance(summary, str)
    assert len(summary) > 10

def test_fact_checker_success():
    with patch("fact_checker.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {"extract": "Artificial Intelligence is..."}
        mock_get.return_value = mock_response

        from fact_checker import fact_check
        summary = fact_check("Artificial Intelligence")
        assert summary == "Artificial Intelligence is..."

def test_fact_checker_missing_extract():
    with patch("fact_checker.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        from fact_checker import fact_check
        summary = fact_check("Artificial Intelligence")
        assert summary == "No summary found."

def test_fact_checker_error():
    with patch("fact_checker.requests.get") as mock_get:
        mock_get.side_effect = Exception("Network error")

        from fact_checker import fact_check
        summary = fact_check("Artificial Intelligence")
        assert summary == "Fact-checking failed."


# ─── Topic Generator Tests ───

def test_topic_generation_returns_suggestions():
    from topic_generator import generate_topics
    themes = ["AI", "healthcare"]
    interests = ["ethics", "automation"]
    suggestions = generate_topics(themes, interests)
    assert isinstance(suggestions, list)
    assert len(suggestions) > 0

def test_generate_strings():
    from topic_generator import generate_topics
    suggestions = generate_topics(["AI"], ["robots"])
    for s in suggestions:
        assert isinstance(s, str)


# ─── Feedback & History (via API) ───

def test_feedback_submit():
    payload = {"suggestion": "Test starter", "action": "thumbs_up"}
    response = client.post("/feedback", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_get_feedback():
    response = client.get("/feedback")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_history():
    response = client.get("/history")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
