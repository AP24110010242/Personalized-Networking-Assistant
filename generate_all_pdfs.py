import os
from fpdf import FPDF

source_dir = r"C:\Users\vijay\Desktop\Personalized Networking Assistant"

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'Personalized Networking Assistant - Project Deliverable', border=False, align='R')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def create_pdf(folder, filename, title, sections):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12)
    
    # Title
    pdf.set_font('helvetica', 'B', 16)
    pdf.set_text_color(33, 37, 41)
    pdf.cell(0, 12, title, new_x="LMARGIN", new_y="NEXT", align='L')
    pdf.ln(5)
    
    # Team info
    pdf.set_font('helvetica', 'I', 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 5, "Team Members: Thrivedh Reddy (Lead), Bhagesh T., Harshavardhan R., Vijay R., Sampath K.", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    
    # Content
    pdf.set_text_color(0, 0, 0)
    for section_title, paragraphs in sections:
        pdf.set_font('helvetica', 'B', 12)
        pdf.cell(0, 8, section_title, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font('helvetica', size=11)
        for p in paragraphs:
            pdf.multi_cell(0, 6, p)
            pdf.ln(2)
        pdf.ln(2)
        
    dest_path = os.path.join(source_dir, folder, filename)
    pdf.output(dest_path)
    print(f"Generated PDF: {folder}/{filename}")

# --- Generate All 22 PDFs ---

# 1
create_pdf("1. Brainstorming & Ideation", "Brainstorming & Idea Prioritization.pdf", "Brainstorming & Idea Prioritization", [
    ("1. Project Ideas Brainstormed", [
        "Resume Customizer: An AI tool matching resumes to job descriptions.",
        "AI Mock Interviewer: Prep tool with speech-to-text feedback.",
        "Personalized Networking Assistant: A system generating tailored starters for events using zero-shot classification and text generation."
    ]),
    ("2. Prioritization & Value Matrix", [
        "We selected the Personalized Networking Assistant because it targets a highly relatable problem (networking anxiety), relies on lightweight local models (DistilBERT/GPT-2) that run easily on CPU without API keys, and has clear modular boundaries for team allocation."
    ])
])

# 2
create_pdf("1. Brainstorming & Ideation", "Define Problem Statements .pdf", "Define Problem Statements", [
    ("1. The Context", [
        "Attendees at conferences, social gatherings, and networking events frequently find it hard to start conversations with strangers or express their interests effectively."
    ]),
    ("2. The Problem Statement", [
        "How might we design a software tool that automatically extracts themes from event descriptions, crafts context-aware icebreakers matching user interests, and verifies topics via Wikipedia in real-time?"
    ])
])

# 3
create_pdf("1. Brainstorming & Ideation", "Empathy Map.pdf", "Empathy Map", [
    ("Says", ["'I don't know what to talk about first.'", "'I hope I don't look isolated.'"]),
    ("Thinks", ["'Everyone else seems to know each other.'", "'I need a quick cheat-sheet.'"]),
    ("Does", ["Stands near the food counter.", "Browses phone to avoid eye contact."]),
    ("Feels", ["Anxious, nervous, but willing to connect."])
])

# 4
create_pdf("2. Requirement Analysis", "Customer Journey Map.pdf", "Customer Journey Map", [
    ("1. Discovers Event", ["User feels anxious and seeks topics to talk about."]),
    ("2. Inputs Event Details", ["User enters event details and interests into the Streamlit app."]),
    ("3. Obtains Prompts", ["App generates 2-3 tailored conversation starters."]),
    ("4. Preparation & Fact-Checking", ["User uses the Wikipedia feature to verify details on topics."]),
    ("5. Connection & Networking", ["User successfully makes contacts at the event."])
])

# 5
create_pdf("2. Requirement Analysis", "Data Flow Diagram.pdf", "Data Flow Diagram", [
    ("Data Flow - Level 0", [
        "User Inputs (Description, Interests) -> Streamlit Web UI -> FastAPI Backend API -> Response JSON (Themes, Starters) -> Streamlit UI."
    ]),
    ("Data Flow - Level 1", [
        "Streamlit UI -> FastAPI APIRouter -> Event Analyzer Service (DistilBERT pipeline) -> Topic Generator Service (GPT-2 generator) -> history.json logging -> Response returned."
    ])
])

# 6
create_pdf("2. Requirement Analysis", "Solution Requirements.pdf", "Solution Requirements", [
    ("1. Functional Requirements", [
        "FR1: The system must classify event descriptions using zero-shot NLP.",
        "FR2: The system must output natural conversation prompts.",
        "FR3: The system must query Wikipedia summaries.",
        "FR4: The system must save execution history and thumbs-up/down ratings."
    ]),
    ("2. Non-Functional Requirements", [
        "NFR1: App must run locally on CPU.",
        "NFR2: Response time should be <1.5 seconds post startup."
    ])
])

# 7
create_pdf("2. Requirement Analysis", "Technology Stack.pdf", "Technology Stack", [
    ("1. Frontend UI", ["Streamlit (v1.38.0) for layouts, inputs, and button callbacks."]),
    ("2. Backend API Server", ["FastAPI (v0.115.12) with Uvicorn server for endpoint execution."]),
    ("3. NLP Models", [
        "DistilBERT (zero-shot) for category scoring.",
        "GPT-2 Small for prompt generation."
    ]),
    ("4. Data Store", ["Local JSON files (history.json, feedback.json) for lightweight tracking."])
])

# 8
create_pdf("3. Project Design Phase", "Problem-Solution Fit.pdf", "Problem-Solution Fit", [
    ("User Pain Points & Solves", [
        "Icebreaker generation matches interests to solve conversation anxiety.",
        "Wikipedia summary fetch solves factual uncertainty.",
        "JSON session logger solves tracking past strategies."
    ])
])

# 9
create_pdf("3. Project Design Phase", "Proposed Solution.pdf", "Proposed Solution", [
    ("Technical Design Architecture", [
        "We proposed and built a clean, modular Python application using FastAPI and Streamlit. The services handle NLP modeling locally on CPU without external API key dependencies."
    ])
])

# 10
create_pdf("3. Project Design Phase", "Solution Architecture.pdf", "Solution Architecture", [
    ("System Tier Architecture", [
        "Tier 1: Client web interface (Streamlit rendering columns, cards, lists).",
        "Tier 2: Backend web server (FastAPI exposing POST endpoints for validation).",
        "Tier 3: Service layers (DistilBERT zero-shot classifier, GPT-2 text-generator, local database write logs)."
    ])
])

# 11
create_pdf("4. Project Planning Phase", "Project Planning.pdf", "Project Planning", [
    ("Project Schedule & Tasks", [
        "Sprint 1: Architecture setup, models configuration (Lead: Thrivedh Reddy).",
        "Sprint 2: Pydantic schemas, routes development (Harshavardhan Gunnamareddy).",
        "Sprint 3: Model pipelines, local logs (Bhagesh Thupakula).",
        "Sprint 4: Streamlit UI construction, columns (Vijay Vintha).",
        "Sprint 5: Test writing, QA (Sampath Kilari)."
    ])
])

# 12
create_pdf("5. Project Development Phase", "Code-Layout, Readability and Reusability.pdf", "Code-Layout, Readability and Reusability", [
    ("1. Code Layout", [
        "Project follows standard python structure: code under app/ folder, frontend UI under frontend/, and pytest suites under tests/."
    ]),
    ("2. Readability", [
        "Used type hints, clear variables, and modularized services (single responsibility principle)."
    ])
])

# 13
create_pdf("5. Project Development Phase", "Coding & Solution.pdf", "Coding & Solution", [
    ("1. Backend Codebase", [
        "FastAPI routes exposed on /analyze-event, /fact-check, and /generate-conversation. Integrated schema validation via Pydantic."
    ]),
    ("2. Frontend Codebase", [
        "Streamlit page handles description textbox, interest text inputs, result lists, feedback buttons, and history reloads."
    ])
])

# 14
create_pdf("5. Project Development Phase", "No. of Functional Features Included in the Solution.pdf", "No. of Functional Features Included in the Solution", [
    ("Functional Features Implemented", [
        "1. Theme classification via zero-shot DistilBERT.",
        "2. Coherent starter prompt generation via GPT-2.",
        "3. Live Wikipedia summary fact-checking.",
        "4. Session audit history logs.",
        "5. Granular thumbs-up/down feedback logger."
    ])
])

# 15
create_pdf("6.Project Testing", "Performance Testing.pdf", "Performance Testing", [
    ("Performance Benchmarks", [
        "Initial load: Slow (downloads DistilBERT & GPT-2 models).",
        "Inference processing: Under 1.5s on standard CPU.",
        "Memory usage: ~1GB RAM overhead for model weights."
    ])
])

# 16
create_pdf("7.Project Documentation", "Project Executable Files.pdf", "Project Executable Files", [
    ("Installation & Run Steps", [
        "1. Create virtual environment: python -m venv .venv",
        "2. Activate venv: .venv\\Scripts\\activate.ps1 (on Windows)",
        "3. Install dependencies: pip install -r requirements.txt",
        "4. Launch backend: uvicorn app.main:app",
        "5. Launch Streamlit UI: streamlit run frontend/streamlit_app.py"
    ])
])

# 17
create_pdf("7.Project Documentation", "Sample Project Documentation.pdf", "Sample Project Documentation", [
    ("Developer Manual Summary", [
        "Contains complete package specifications, data schemas (ConversationRequest, ConversationResponse), and API routing lifecycle details."
    ])
])

# 18
create_pdf("8.Project Demonstration", "Communication.pdf", "Communication", [
    ("Collaboration Communication", [
        "The team collaborated using Git branches (feature/*) and GitHub Pull Requests to review and merge code into main."
    ])
])

# 19
create_pdf("8.Project Demonstration", "Demonstration of Proposed Features.pdf", "Demonstration of Proposed Features", [
    ("Demo Flow Tasks", [
        "1. Start FastAPI server and show interactive Swagger documentation.",
        "2. Input sample parameters in Streamlit UI.",
        "3. Show AI starters and thumbs up feedback logging.",
        "4. Demonstrate Wikipedia fact checking."
    ])
])

# 20
create_pdf("8.Project Demonstration", "Project Demo Planning.pdf", "Project Demo Planning", [
    ("Presentation Schedule", [
        "Introduction: 2 mins.",
        "Architecture & Model selections: 3 mins.",
        "Live Demo: 5 mins.",
        "Code Structure & Tests: 3 mins.",
        "Q&A: 2 mins."
    ])
])

# 21
create_pdf("8.Project Demonstration", "Scalability & Future Plan.pdf", "Scalability & Future Plan", [
    ("Scalability roadmap", [
        "1. Upgrade to Gemini API for high quality prompt suggestions.",
        "2. Implement PostgreSQL database.",
        "3. Deploy on containerized Docker cluster."
    ])
])

# 22
create_pdf("8.Project Demonstration", "Team Involvement in Demonstration.pdf", "Team Involvement in Demonstration", [
    ("Presenters Breakdown", [
        "Thrivedh Reddy: Introduction & Demo Lead.",
        "Bhagesh T. & Harshavardhan R.: Model configurations & Backend API.",
        "Vijay R. & Sampath K.: Streamlit UI & QA testing."
    ])
])

print("All 22 project PDFs generated successfully!")
