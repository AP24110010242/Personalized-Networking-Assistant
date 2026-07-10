from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from event_analyzer import extract_event_themes
from topic_generator import generate_topics
from fact_checker import fact_check

import json
import threading
from datetime import datetime, timezone
from pathlib import Path
import uuid

app = FastAPI(title="Personalized Networking Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data file paths ---
DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
HISTORY_FILE = DATA_DIR / "history.json"
FEEDBACK_FILE = DATA_DIR / "feedback.json"
_lock = threading.Lock()


# --- Pydantic Schemas ---
class EventInput(BaseModel):
    description: str

class ConversationRequest(BaseModel):
    description: str
    interests: List[str]

class ConversationResponse(BaseModel):
    topics: List[str]
    suggestions: List[str]

class FactCheckRequest(BaseModel):
    query: str

class FactCheckResponse(BaseModel):
    summary: str

class FeedbackRequest(BaseModel):
    suggestion: str
    action: str

class FeedbackResponse(BaseModel):
    status: str


# --- Helper: History logging ---
def _load_json(filepath: Path) -> list:
    with _lock:
        if filepath.exists():
            with open(filepath, "r") as f:
                return json.load(f)
        return []

def _save_json(filepath: Path, data: list):
    with _lock:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

def log_conversation(entry: dict):
    history = _load_json(HISTORY_FILE)
    history.append(entry)
    _save_json(HISTORY_FILE, history)

def log_feedback(entry: dict):
    feedback = _load_json(FEEDBACK_FILE)
    feedback.append(entry)
    _save_json(FEEDBACK_FILE, feedback)


# --- API Endpoints ---
@app.get("/")
def root():
    return {"message": "Welcome to the Networking Assistant API!"}

@app.post("/analyze-event")
def analyze_event(data: EventInput):
    themes = extract_event_themes(data.description)
    return {"topics": themes}

@app.post("/generate-conversation", response_model=ConversationResponse)
def generate_conversation(data: ConversationRequest):
    themes = extract_event_themes(data.description)
    suggestions = generate_topics(themes, data.interests)

    conv_id = f"conv_{uuid.uuid4().hex[:8]}"
    starters = []
    for s in suggestions:
        starters.append({
            "id": f"starter_{uuid.uuid4().hex[:8]}",
            "starter": s
        })

    entry = {
        "id": conv_id,
        "type": "conversation_generation",
        "event_description": data.description,
        "themes": themes,
        "interests": data.interests,
        "content": {
            "conversation_starters": starters
        },
        "num_generated": len(suggestions),
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    log_conversation(entry)

    return ConversationResponse(topics=themes, suggestions=suggestions)

@app.post("/fact-check", response_model=FactCheckResponse)
def fact_check_endpoint(data: FactCheckRequest):
    summary = fact_check(data.query)
    return FactCheckResponse(summary=summary)

@app.post("/feedback", response_model=FeedbackResponse)
def submit_feedback(data: FeedbackRequest):
    entry = {
        "id": f"feedback_{uuid.uuid4().hex[:8]}",
        "item_id": data.suggestion,
        "feedback_type": data.action,
        "notes": data.suggestion,
        "submitted_at": datetime.now(timezone.utc).isoformat()
    }
    log_feedback(entry)
    return FeedbackResponse(status="ok")

@app.get("/feedback")
def get_feedback():
    data = _load_json(FEEDBACK_FILE)
    return data[-10:] if data else []

@app.get("/history")
def get_history():
    data = _load_json(HISTORY_FILE)
    return data[-5:] if data else []
