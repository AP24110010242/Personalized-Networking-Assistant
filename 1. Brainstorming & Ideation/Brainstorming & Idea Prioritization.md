# Brainstorming & Idea Prioritization

### 1. Brainstormed Project Ideas
Our team brainstormed multiple ideas to solve problems using AI/ML:
1. **Resume Customizer:** An AI tool that matches a resume to a job description.
2. **AI Mock Interviewer:** An interactive speech-to-text interview prep tool.
3. **Personalized Networking Assistant (Selected):** A web app that analyzes networking event descriptions and interests to generate smart icebreakers and verify topics via Wikipedia.

### 2. Idea Prioritization Matrix
We evaluated the ideas based on feasibility, utility, and development speed:
- **Resume Customizer:** Useful, but required complex parsing of PDF/Word documents.
- **AI Mock Interviewer:** High complexity due to audio APIs.
- **Personalized Networking Assistant:** High utility (helps students and professionals network), high feasibility (uses lightweight local transformer models on CPU), and allows modular division of tasks (Streamlit frontend, FastAPI backend, local NLP pipelines).

### 3. Decision
We prioritized the **Personalized Networking Assistant** because it addresses a major pain point (networking anxiety) and fits perfectly within a CPU-friendly, local transformer deployment environment.
