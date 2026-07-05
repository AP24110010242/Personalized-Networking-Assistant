# Solution Requirements

### 1. Functional Requirements
- **FR1:** The system must accept event descriptions and user interests as text inputs.
- **FR2:** The system must classify event descriptions into 3 main themes using a zero-shot classification model.
- **FR3:** The system must generate 3 natural conversation starters matching themes and interests.
- **FR4:** The system must query Wikipedia's API for summarized text on user queries.
- **FR5:** The system must log conversation runs and thumbs-up/down ratings to JSON files.

### 2. Non-Functional Requirements
- **NFR1 (Performance):** Average generation request processing (post-model loading) should take less than 1.5 seconds.
- **NFR2 (Usability):** The interface must be responsive, clean, and intuitive.
- **NFR3 (Deployment):** The app must run completely locally on a standard CPU machine without requiring external paid keys (e.g. OpenAI/Gemini).
