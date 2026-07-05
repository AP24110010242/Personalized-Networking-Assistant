# Proposed Solution

The **Personalized Networking Assistant** is structured as a modular, three-tier Python application:

1. **API Layer (FastAPI):**
   - Handles request JSON parsing.
   - Validates data formats using Pydantic schemas.
   - Triggers service layers and logs outputs.
2. **Service Layer (Python Modules):**
   - `event_analyzer.py` handles DistilBERT pipelines.
   - `topic_generator.py` handles GPT-2 text generation.
   - `fact_checker.py` handles HTTP calls to Wikipedia.
   - `history_logger.py`/`feedback_logger.py` handle JSON file reads/writes.
3. **UI Layer (Streamlit):**
   - Captures text area inputs.
   - Renders columns, loaders, fact-check boxes, and history toggles.
