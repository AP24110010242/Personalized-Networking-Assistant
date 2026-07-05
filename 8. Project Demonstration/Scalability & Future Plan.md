# Scalability & Future Plan

### 1. Cloud Deployment
- **Hosting:** Deploy the FastAPI backend on **Render** or **AWS ECS** and host the Streamlit UI on **Streamlit Community Cloud**.
- **Containerization:** Create a `Dockerfile` to package python dependencies and model caches for consistent environment runs.

### 2. Upgrading AI Models
- Transition from local `GPT-2` to a remote LLM API (e.g. **Google Gemini API**) for higher-quality, context-aware icebreakers.

### 3. Database Migration
- Replace `history.json` and `feedback.json` with a PostgreSQL database connected via SQLAlchemy ORM for multi-user scaling.
