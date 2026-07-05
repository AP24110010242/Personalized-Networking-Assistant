# Technology Stack

We chose a robust, lightweight, and modern stack:

1. **Frontend: Streamlit**
   - *Why:* Python-based frontend framework that enables extremely fast UI development, native layout structures (columns), and session state management.
2. **Backend: FastAPI**
   - *Why:* High-performance REST API framework with automatic type validation via Pydantic and built-in interactive Swagger documentation.
3. **AI/ML Layer: Hugging Face Transformers**
   - *Classifier:* `DistilBERT` (zero-shot classification) — selected for speed and accuracy in extracting categories without custom training.
   - *Generator:* `GPT-2 Small` — selected for generation of coherent text starters running efficiently on CPU.
4. **Data Verification: Wikipedia REST API**
   - *Why:* Free, reliable, and requires no API keys or setup overhead.
