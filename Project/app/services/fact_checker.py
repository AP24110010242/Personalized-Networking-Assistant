import requests
from app.config import FACT_CHECK_API

import urllib.parse

def fact_check(query: str) -> str:
    try:
        # Clean up the query: remove surrounding quotes and replace spaces with underscores
        clean_query = query.strip('"' + "'").replace(" ", "_")
        encoded_query = urllib.parse.quote(clean_query)
        
        headers = {
            "User-Agent": "PersonalizedNetworkingAssistant/1.0 (https://github.com/AP24110010242/Personalized-Networking-Assistant) Python/requests"
        }
        response = requests.get(f"{FACT_CHECK_API}/{encoded_query}", headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("extract", "No summary found.")
        else:
            return f"Topic not found on Wikipedia (or API error {response.status_code})."
    except Exception as e:
        return f"Fact-checking failed. ({e})"
