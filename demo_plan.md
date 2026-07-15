# 🎬 Personalized Networking Assistant — 5-Minute Demo Plan

> **Team**: 2 Members
> **Total Duration**: 5:00 minutes | **4 Parts split across 2 Members**

---

## 📋 Part Allocation

| Part | Duration | Presenter | Content |
|------|----------|-----------|---------|
| **Part 1** — Introduction | 0:00 – 1:00 (60s) | **Member 1** | Problem, solution overview, team intro |
| **Part 2** — Backend & Frontend | 1:00 – 2:30 (90s) | **Member 1** | Architecture, tech stack, code walkthrough |
| **Part 3** — Live Demo | 2:30 – 4:15 (105s) | **Member 2** | Live walkthrough of all features |
| **Part 4** — Conclusion | 4:15 – 5:00 (45s) | **Member 2** | Summary, scalability, future scope, thank you |

> [!TIP]
> **Member 1** handles the conceptual/technical explanation (Parts 1 & 2 — ~2:30 total).
> **Member 2** handles the hands-on demo and wrap-up (Parts 3 & 4 — ~2:30 total).
> This gives each member an equal ~2.5 minutes.

---

## 🎙️ Part 1: Introduction (0:00 – 1:00) — Member 1

### What to Show on Screen
- Project title slide or the Streamlit app's hero banner
- Flash the **Architecture Diagram** briefly at the end

### Script / Talking Points

> *"Hello everyone, I'm [Name] and along with [Partner's Name], we're presenting our project — the **Personalized Networking Assistant**."*
>
> *"**The Problem**: In professional networking events, people often struggle to initiate meaningful conversations — they don't know what topics to bring up or how to break the ice."*
>
> *"**Our Solution**: We built an AI-powered web application that analyzes event descriptions, extracts key discussion themes using **NLP**, and generates **personalized conversation starters** based on the user's interests."*
>
> *"The app also provides **Wikipedia-based fact verification**, maintains a **session history**, and collects **user feedback** — all through a modern, premium web interface."*
>
> *"Let me now walk you through the architecture and code behind this."*

---

## 🏗️ Part 2: Backend & Frontend (1:00 – 2:30) — Member 1

### 2A: Architecture & Tech Stack (~50 seconds)

#### What to Show on Screen
- **Architecture Diagram** → **Tech Stack Image** → **Data Flow Diagram**

#### Script / Talking Points

> *"Our project follows a **client-server architecture**."*
>
> *"The **frontend** is built with **Streamlit** — providing an interactive dark-themed UI with glassmorphic design."*
>
> *"The **backend** uses **FastAPI**, exposing REST API endpoints for event analysis, conversation generation, fact-checking, history, and feedback."*
>
> *"For **AI/ML**, we use two **Hugging Face Transformer** models:*
> - ***DistilBERT** — for zero-shot classification to extract the top 3 event themes*
> - ***GPT-2** — for generating personalized conversation starters"*
>
> *"We also integrate the **Wikipedia REST API** for fact verification, and use **JSON files** for data persistence. The entire app is **Dockerized** and deployable on **Render**."*

**Architecture Diagram:**

![Architecture Diagram](C:\Users\vijay\.gemini\antigravity-ide\brain\4f017b10-18b4-4ce8-8f0e-e509f04b69d2\architecture_diagram_1784041050765.png)

**Tech Stack:**

![Tech Stack](C:\Users\vijay\.gemini\antigravity-ide\brain\4f017b10-18b4-4ce8-8f0e-e509f04b69d2\tech_stack_1784041060529.png)

**Data Flow:**

![Data Flow](C:\Users\vijay\.gemini\antigravity-ide\brain\4f017b10-18b4-4ce8-8f0e-e509f04b69d2\data_flow_1784041069081.png)

---

### 2B: Code Walkthrough (~40 seconds)

#### What to Show on Screen
- Quickly flash through key code files in VS Code

#### Script / Talking Points

> *"Let me quickly walk through the code structure."*
>
> *"Our backend is **modular** — `main.py` initializes the FastAPI app, `conversation.py` defines all 6 API endpoints, and the `services/` folder has separate modules for each feature:"*
> - *"`event_analyzer.py` — loads DistilBERT for zero-shot classification"*
> - *"`topic_generator.py` — loads GPT-2 for conversation generation"*
> - *"`fact_checker.py` — calls the Wikipedia API"*
> - *"`schemas.py` — Pydantic models for input/output validation"*
>
> *"The frontend is a single Streamlit app with **4 tabs** — Generate Starters, Fact Check, History, and Feedback."*
>
> *"We've written **Pytest unit tests** for all services. Now let me hand it over to [Member 2] for the live demo."*

#### Key Files to Flash (in order)

| File | What to Highlight |
|------|-------------------|
| [main.py](file:///c:/Users/vijay/Desktop/Personalized%20Networking%20Assistant/Project/app/main.py) | FastAPI app init + router |
| [conversation.py](file:///c:/Users/vijay/Desktop/Personalized%20Networking%20Assistant/Project/app/routers/conversation.py) | 6 REST API endpoints |
| [event_analyzer.py](file:///c:/Users/vijay/Desktop/Personalized%20Networking%20Assistant/Project/app/services/event_analyzer.py) | DistilBERT zero-shot pipeline |
| [topic_generator.py](file:///c:/Users/vijay/Desktop/Personalized%20Networking%20Assistant/Project/app/services/topic_generator.py) | GPT-2 generation pipeline |
| [fact_checker.py](file:///c:/Users/vijay/Desktop/Personalized%20Networking%20Assistant/Project/app/services/fact_checker.py) | Wikipedia API call |
| [schemas.py](file:///c:/Users/vijay/Desktop/Personalized%20Networking%20Assistant/Project/app/models/schemas.py) | Pydantic validation models |
| [streamlit_app.py](file:///c:/Users/vijay/Desktop/Personalized%20Networking%20Assistant/Project/frontend/streamlit_app.py) | 4-tab UI with glassmorphic CSS |

---

## 🖥️ Part 3: Live Demo (2:30 – 4:15) — Member 2

> [!IMPORTANT]
> **Pre-Demo Checklist:**
> - Start backend: `uvicorn app.main:app --reload`
> - Start frontend: `streamlit run frontend/streamlit_app.py`
> - **Run the app once** before recording so AI models are cached in memory
> - Have the sample input below ready to copy-paste

### Demo Flow

#### Step 1: Show the Landing Page (~10s)
> *"Thanks [Member 1]. Here's our Networking Assistant running live — you can see the dark-themed glassmorphic UI with the hero banner, sidebar stats, and 4 feature tabs."*

#### Step 2: Generate Conversation Starters (~40s)
> *"Let me demonstrate the core feature."*

**Paste this sample input:**
```
Event Description:
"Global AI Summit 2026 — A two-day conference exploring the intersection 
of artificial intelligence, healthcare innovation, and sustainable technology. 
Featuring keynote speakers from Google DeepMind and OpenAI."

Interests: machine learning, healthcare AI, climate tech
```

- Paste the event description → enter interests → click **"✨ Generate Starters"**
- Show the spinner while AI processes
- Point out the **extracted themes** (topic pills: AI, healthcare, sustainability)
- Point out the **generated conversation starters** (numbered cards)

#### Step 3: Feedback Feature (~15s)
> *"Users can rate each starter with thumbs up or down — this gets logged for future improvement."*
- Click 👍 on one starter, 👎 on another

#### Step 4: Fact-Check Feature (~20s)
> *"Let me fact-check a topic using our Wikipedia integration."*
- Switch to **🔍 Fact Check** tab
- Type `"artificial intelligence"` → show the Wikipedia summary

#### Step 5: History & Feedback Tabs (~15s)
> *"The app maintains complete session history and all user feedback."*
- Switch to **📜 History** tab → show past sessions
- Switch to **📊 Feedback** tab → show logged feedback entries

#### Step 6: FastAPI Docs (Optional, ~5s)
> *"And our backend provides auto-generated Swagger API docs."*
- Flash `http://127.0.0.1:8000/docs`

---

## 🎯 Part 4: Conclusion & Future Scope (4:15 – 5:00) — Member 2

### Script / Talking Points

> *"To summarize, we built an end-to-end AI-powered networking assistant that:*
> - *Analyzes events with **DistilBERT** zero-shot classification*
> - *Generates conversation starters with **GPT-2***
> - *Verifies facts via **Wikipedia API***
> - *Logs history and collects feedback*
> - *Has a modern **Streamlit** frontend with **FastAPI** backend*
> - *Is fully tested with **Pytest** and deployable with **Docker + Render**"*

> *"For **future enhancements**, we plan to:*
> - *Upgrade to more powerful LLMs like **Llama or GPT-4***
> - *Add **user authentication** and profile management*
> - *Move from JSON to **PostgreSQL** database*
> - *Integrate real-time events from **Eventbrite** and **Meetup***
> - *Build a **mobile-responsive PWA** version"*

> *"Thank you for watching! We're happy to take any questions."*

---

## 📊 Visual Assets Summary

| Asset | When to Show | Image |
|-------|-------------|-------|
| Architecture Diagram | Part 1 end / Part 2A | Show during architecture explanation |
| Tech Stack | Part 2A | Show alongside architecture |
| Data Flow | Part 2A | Show the pipeline flow |
| Code Files | Part 2B | Flash in VS Code |
| Live App (Streamlit) | Part 3 | Full live demo |
| Swagger Docs | Part 3 (optional) | FastAPI auto-docs |

---

## 💡 Recording Tips

> [!WARNING]
> DistilBERT and GPT-2 models take **10-30 seconds to load on first call**. Run the app once before recording so models are cached. Otherwise your demo will have an awkward wait!

1. **Use OBS Studio or Loom** for screen + audio recording
2. **Zoom in** (Ctrl +) on code and UI so it's readable on video
3. **Keep a clean desktop** — close unnecessary apps/tabs
4. **Practice once together** — aim for ~4:30 so you have 30s buffer
5. **Speak clearly at moderate pace** — 5 minutes goes fast!
6. **Smooth handoff**: Member 1 says *"Let me hand it over to [name]"* → Member 2 says *"Thanks [name]"*
