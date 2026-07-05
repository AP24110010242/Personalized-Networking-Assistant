# Customer Journey Map

### Phase 1: Pre-Event Prep (Anxiety)
- **User Action:** Reviewing the event description and feeling unsure how to connect their interests.
- **User Feeling:** Overwhelmed, nervous.
- **App Touchpoint:** Opens the Streamlit frontend.

### Phase 2: Generation (Utility)
- **User Action:** Enters event description and interests, clicks "Generate Conversation Starters".
- **User Feeling:** Hopeful, engaged.
- **App Touchpoint:** Streamlit sends a payload to FastAPI backend, which processes the event via DistilBERT and generates starters using GPT-2.

### Phase 3: Fact-Checking (Confidence)
- **User Action:** Types a topic to verify and hits "Fact Check".
- **User Feeling:** Relieved, informed.
- **App Touchpoint:** App displays Wikipedia API summaries in real-time.

### Phase 4: Active Networking (Success)
- **User Action:** Uses the generated starters to network successfully.
- **User Feeling:** Confident, accomplished.
- **App Touchpoint:** Rates suggestions (👍/👎) to save feedback for future sessions.
