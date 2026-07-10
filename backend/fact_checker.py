import requests
from urllib.parse import quote

FACT_CHECK_API = "https://en.wikipedia.org/api/rest_v1/page/summary"

def fact_check(query: str) -> str:
    """Fact-check a topic by querying the Wikipedia REST API for a summary."""
    try:
        encoded_query = quote(query, safe="")
        headers = {"User-Agent": "PersonalizedNetworkingAssistant/1.0 (contact@example.com)"}
        response = requests.get(f"{FACT_CHECK_API}/{encoded_query}", headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("extract", "No summary found.")
    except requests.exceptions.RequestException as e:
        return f"Fact-checking failed: {e}"
    except Exception:
        return "Fact-checking failed."
