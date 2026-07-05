# Data Flow Diagram (DFD)

```
[User Interface (Streamlit)]
       │
       ▼ (POST /generate-conversation)
[API Router (FastAPI)]
       │
       ├──► [Event Analyzer (DistilBERT Zero-shot)] ──► Extracts Top 3 Themes
       │
       ├──► [Topic Generator (GPT-2 Text Generation)] ──► Generates 3 Icebreakers
       │
       ├──► [History Logger Service] ──► Appends to history.json
       │
       ▼ (JSON Response)
[User Interface (Streamlit)]
```

### Fact-Checking Flow:
```
[User Interface (Streamlit)] ──(POST /fact-check)──► [FastAPI Router] ──► [Wikipedia REST API] ──► [Success Box]
```
