from unittest.mock import patch, MagicMock
from app.services import fact_checker

def test_fact_checker_returns_summary():
    # Make a real call (will use internet, but tests are fast)
    summary = fact_checker.fact_check("Artificial Intelligence")
    assert isinstance(summary, str)
    assert len(summary) > 10

def test_fact_checker_success():
    with patch("app.services.fact_checker.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {"extract": "Artificial Intelligence is..."}
        mock_get.return_value = mock_response
        
        summary = fact_checker.fact_check("Artificial Intelligence")
        assert summary == "Artificial Intelligence is..."

def test_fact_checker_missing_extract():
    with patch("app.services.fact_checker.requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response
        
        summary = fact_checker.fact_check("Artificial Intelligence")
        assert summary == "No summary found."

def test_fact_checker_error():
    with patch("app.services.fact_checker.requests.get") as mock_get:
        mock_get.side_effect = Exception("Network error")
        
        summary = fact_checker.fact_check("Artificial Intelligence")
        assert summary == "Fact-checking failed."
