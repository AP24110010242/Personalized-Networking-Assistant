# Personalized Networking Assistant

An AI-powered web application that helps users generate smart, tailored conversation starters for professional or social networking events. 

This project is built using a modern AI/ML stack, running local models via Hugging Face Transformers for natural language understanding and text generation, and exposing an interactive web dashboard built with Streamlit and FastAPI.

---

## 👥 Team Members & Roles

* **Thrivedh Reddy** — *Team Lead / Lead Architect*
  * Designed the overall application architecture, centralized routing, and request validation flows.
* **Bhagesh Thupakula** (AP24110011158) — *AI & ML Services Engineer*
  * Configured local AI pipelines, including the DistilBERT classifier and GPT-2 prompt engineering.
* **Harshavardhan Reddy Gunnamareddy** — *Backend Developer*
  * Developed the FastAPI endpoints, Wikipedia fact-checker utility, and HTTP network integrations.
* **Vijay Reddy Vintha** — *Frontend UI Developer*
  * Designed the Streamlit dashboard user interface, interactive layouts, columns, and session state management.
* **Sampath Kilari** — *QA & Logging Engineer*
  * Implemented append-only JSON logging for history and feedback, and authored the pytest automated test suites.

---

## 🌟 Core Scenarios & Features

### 1. Generating Smart Starters
Users input a description of a networking event (e.g., *"AI for Sustainable Cities"*) and specify their personal interests (e.g., *"climate change, urban planning"*). 
* **Backend Pipeline:** The backend zero-shot classifier (DistilBERT) extracts the 3 most relevant professional themes. It passes these themes and interests into a context prompt.
* **Generation:** GPT-2 generates up to 3 creative, tailored conversation starters.
* **Storage:** The session is automatically saved to the persistent history logs.

### 2. Quick Fact Verification
Users preparing for an event can verify claims or topics (e.g., *"blockchain in healthcare"*) on the fly.
* **Endpoint:** The app queries the Wikipedia REST API to retrieve a reliable, summarized reference extract.

### 3. Reviewing Past Strategies (History & Feedback)
* **History Log:** Users can reload the last 5 conversations generated to review past starters via the `/history` API endpoint.
* **Feedback System:** Users can review the last 10 suggestions they rated with thumbs-up (liked) or thumbs-down (disliked) via the `/feedback` API endpoint, enabling analytics for prompt tuning.

---

## 📁 Repository Structure

```
├── backend/                             # FastAPI Backend
│   ├── data/                            # Persistent JSON data storage
│   │   ├── feedback.json               # User feedback entries
│   │   └── history.json                # Conversation generation history
│   ├── tests/                           # Python Pytest Suite
│   │   └── test_backend.py             # All backend tests
│   ├── app.py                           # FastAPI app, routes & schemas
│   ├── event_analyzer.py               # DistilBERT zero-shot classifier
│   ├── fact_checker.py                  # Wikipedia fact-check service
│   └── topic_generator.py              # GPT-2 conversation starter generator
├── frontend/                            # Streamlit Frontend UI
│   └── streamlit_app.py                # Professional glassmorphism dashboard
├── GIT/                                 # 8 Phase Project Documentation Folders
│   ├── 1. Brainstorming & Ideation/     # Problem Statements, Empathy Map, Idea Prioritization
│   ├── 2. Requirement Analysis/         # Customer Journey, DFD, Tech Stack, Requirements
│   ├── 3. Project Design Phase/         # Problem-Solution Fit, Proposed Solution, Solution Architecture
│   ├── 4. Project Planning Phase/       # Project Planning (Sprint Backlog)
│   ├── 5. Project Development Phase/    # Code-Layout, Coding & Solution, Features List
│   ├── 6. Project Testing/              # Performance Testing, test_results.txt
│   ├── 7. Project Documentation/        # Project Executable Files, Sample Doc
│   └── 8. Project Demonstration/        # Communication, Demo Proposed Features, Demo Planning, Scalability, Team Involvement
├── .env                                 # Environment variables
├── .gitignore                           # Git ignore rules
├── README.md                            # Project documentation
└── requirements.txt                     # Project dependencies
```

---

## ⚙️ How to Run Locally

### Prerequisites
- Python 3.10+
- Git

### Step-by-Step Execution

1. **Set Up the Virtual Environment:**
   ```bash
   python -m venv venv
   ```
2. **Activate the Environment:**
   * **Windows (Command Prompt):**
     ```cmd
     venv\Scripts\activate.bat
     ```
   * **Windows (PowerShell):**
     ```powershell
     venv\Scripts\Activate.ps1
     ```
   * **macOS / Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install torch --index-url https://download.pytorch.org/whl/cpu
   pip install -r requirements.txt
   ```

4. **Run the FastAPI Backend Server:**
   ```bash
   cd backend
   uvicorn app:app --reload
   ```
   *(The backend server will run at http://127.0.0.1:8000. You can view interactive Swagger documentation at http://127.0.0.1:8000/docs)*

5. **Run the Streamlit Frontend UI:**
   In a new terminal window (with the virtual environment activated), run:
   ```bash
   streamlit run frontend/streamlit_app.py
   ```
   *(The web interface will open automatically in your browser at http://localhost:8501)*

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message |
| `POST` | `/analyze-event` | Extract themes from event description |
| `POST` | `/generate-conversation` | Generate conversation starters |
| `POST` | `/fact-check` | Fact-check a topic via Wikipedia |
| `POST` | `/feedback` | Submit feedback (like/dislike) for a suggestion |
| `GET` | `/feedback` | Retrieve last 10 feedback entries |
| `GET` | `/history` | Retrieve last 5 conversation sessions |

---

## 🧪 Running Automated Tests
To run the automated `pytest` suite verifying all services, endpoints, and mocking APIs, run:
```bash
cd backend
pytest tests/test_backend.py -v
```
