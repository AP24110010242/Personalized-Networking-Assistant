import streamlit as st
import requests

# ─── Page Config ───
st.set_page_config(
    page_title="Networking Assistant ✨",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_URL = "http://127.0.0.1:8000"

# ─── Custom CSS: Glassmorphism + Professional Styling ───
st.markdown("""
<style>
    /* ── Import Google Fonts ── */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

    /* ── Global ── */
    html, body, [class*="st-"] {
        font-family: 'Outfit', 'Inter', sans-serif !important;
    }

    .stApp {
        background-color: #030303 !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.12) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(168, 85, 247, 0.12) 0px, transparent 50%),
            radial-gradient(at 50% 100%, rgba(59, 130, 246, 0.1) 0px, transparent 50%) !important;
        background-attachment: fixed !important;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background-color: #080808 !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.05) 0px, transparent 50%) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #e0e0ff !important;
    }

    /* ── Glass Card ── */
    .glass-card {
        background: rgba(20, 20, 25, 0.6) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        padding: 32px;
        margin-bottom: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3), 
                    inset 0 1px 0 0 rgba(255, 255, 255, 0.05);
        transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), 
                    box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), 
                    border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        overflow: hidden;
    }

    .glass-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: -150%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            rgba(255, 255, 255, 0) 0%,
            rgba(255, 255, 255, 0.01) 30%,
            rgba(255, 255, 255, 0.12) 50%,
            rgba(255, 255, 255, 0.01) 70%,
            rgba(255, 255, 255, 0) 100%
        );
        transform: skewX(-25deg);
        pointer-events: none;
    }

    .glass-card:hover {
        transform: translateY(-4px);
        border-color: rgba(139, 92, 246, 0.35);
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45), 
                    0 0 15px rgba(139, 92, 246, 0.15),
                    inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
    }

    .glass-card:hover::before {
        left: 150%;
        transition: left 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* ── Hero Banner ── */
    .hero-banner {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.12) 0%, rgba(168, 85, 247, 0.12) 50%, rgba(236, 72, 153, 0.12) 100%);
        backdrop-filter: blur(30px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 48px 40px;
        margin-bottom: 32px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(99, 102, 241, 0.15);
        position: relative;
        overflow: hidden;
        transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), 
                    box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), 
                    border-color 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .hero-banner::before {
        content: "";
        position: absolute;
        top: 0;
        left: -150%;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            90deg,
            rgba(255, 255, 255, 0) 0%,
            rgba(255, 255, 255, 0.01) 30%,
            rgba(255, 255, 255, 0.15) 50%,
            rgba(255, 255, 255, 0.01) 70%,
            rgba(255, 255, 255, 0) 100%
        );
        transform: skewX(-25deg);
        pointer-events: none;
    }

    .hero-banner:hover {
        transform: translateY(-2px);
        border-color: rgba(168, 85, 247, 0.4);
        box-shadow: 0 16px 40px rgba(99, 102, 241, 0.25);
    }

    .hero-banner:hover::before {
        left: 150%;
        transition: left 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .hero-banner h1 {
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #a78bfa, #818cf8, #c084fc, #e879f9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 12px !important;
        letter-spacing: -0.5px;
        position: relative;
        z-index: 2;
    }

    .hero-subtitle {
        color: rgba(200, 200, 230, 0.8);
        font-size: 1.1rem;
        font-weight: 300;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
        position: relative;
        z-index: 2;
    }

    /* ── Section Header ── */
    .section-header {
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        color: #c4b5fd !important;
        margin-bottom: 16px !important;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* ── Starter Card ── */
    .starter-card {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.08), rgba(168, 85, 247, 0.08));
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 16px;
        padding: 20px 24px;
        margin-bottom: 12px;
        color: #e0e0ff;
        font-size: 1rem;
        line-height: 1.6;
        transition: all 0.3s ease;
    }

    .starter-card:hover {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.14), rgba(168, 85, 247, 0.14));
        border-color: rgba(139, 92, 246, 0.4);
        transform: translateX(4px);
    }

    .starter-number {
        display: inline-block;
        background: linear-gradient(135deg, #6366f1, #a855f7);
        color: white;
        font-weight: 700;
        font-size: 0.8rem;
        width: 28px;
        height: 28px;
        line-height: 28px;
        text-align: center;
        border-radius: 50%;
        margin-right: 12px;
    }

    /* ── Topic Pill ── */
    .topic-pill {
        display: inline-block;
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.2));
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 30px;
        padding: 6px 18px;
        margin: 4px 6px 4px 0;
        color: #c4b5fd;
        font-size: 0.85rem;
        font-weight: 500;
        letter-spacing: 0.3px;
    }

    /* ── History Card ── */
    .history-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 16px;
        transition: all 0.3s ease;
    }

    .history-card:hover {
        background: rgba(255, 255, 255, 0.06);
        border-color: rgba(255, 255, 255, 0.1);
    }

    .history-timestamp {
        color: rgba(168, 162, 200, 0.7);
        font-size: 0.8rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .history-event {
        color: #e0e0ff;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 10px;
    }

    .history-detail {
        color: rgba(200, 200, 230, 0.6);
        font-size: 0.9rem;
    }

    /* ── Feedback Pill ── */
    .feedback-item {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .feedback-icon {
        font-size: 1.5rem;
    }

    .feedback-text {
        color: #d0d0e8;
        font-size: 0.95rem;
        flex: 1;
    }

    .feedback-time {
        color: rgba(168, 162, 200, 0.5);
        font-size: 0.75rem;
    }

    /* ── Fact Check Result ── */
    .fact-result {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.08), rgba(16, 185, 129, 0.08));
        border: 1px solid rgba(34, 197, 94, 0.2);
        border-radius: 16px;
        padding: 24px;
        color: #a7f3d0;
        line-height: 1.7;
        font-size: 0.95rem;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 10px 28px !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.3px;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4) !important;
    }

    .stButton > button:active {
        transform: translateY(0px) !important;
    }

    /* ── Text Inputs ── */
    /* ── Text Inputs ── */
    .stTextArea textarea, .stTextInput input, div[data-baseweb="input"] input, div[data-baseweb="textarea"] textarea {
        background: #101014 !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        padding: 12px 16px !important;
        transition: all 0.3s ease !important;
    }

    .stTextArea textarea:focus, .stTextInput input:focus, div[data-baseweb="input"]:focus-within, div[data-baseweb="textarea"]:focus-within {
        border-color: rgba(139, 92, 246, 0.6) !important;
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2) !important;
        background: #08080c !important;
    }

    /* Force text color in wrapper */
    div[data-baseweb="input"], div[data-baseweb="textarea"] {
        background-color: transparent !important;
        border: none !important;
        color: #ffffff !important;
    }

    /* Placeholder style */
    ::placeholder, .stTextArea textarea::placeholder, .stTextInput input::placeholder {
        color: rgba(200, 200, 230, 0.4) !important;
        -webkit-text-fill-color: rgba(200, 200, 230, 0.4) !important;
        opacity: 1 !important;
    }

    .stTextArea label, .stTextInput label {
        color: #c4b5fd !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.3px;
        margin-bottom: 8px !important;
    }

    /* ── Divider ── */
    .custom-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.3), transparent);
        margin: 32px 0;
        border: none;
    }

    /* ── Tabs styling ── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 14px;
        padding: 4px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 10px !important;
        color: #a0a0c0 !important;
        font-weight: 500 !important;
        padding: 10px 20px !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.2)) !important;
        color: #c4b5fd !important;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        display: none;
    }

    /* ── Alert boxes ── */
    .stAlert {
        border-radius: 12px !important;
    }

    /* ── Spinner ── */
    .stSpinner > div {
        border-top-color: #8b5cf6 !important;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(139, 92, 246, 0.3); border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(139, 92, 246, 0.5); }

    /* ── Hide Streamlit branding ── */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    /* ── Metric cards ── */
    .metric-card {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px 24px;
        text-align: center;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #a78bfa, #e879f9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .metric-label {
        color: rgba(200, 200, 230, 0.6);
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 4px;
    }

    /* ── Accordion Glass Expander ── */
    div[data-testid="stExpander"] {
        background: rgba(20, 20, 25, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        border-radius: 16px !important;
        margin-bottom: 12px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2) !important;
        overflow: hidden !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stExpander"]:hover {
        border-color: rgba(139, 92, 246, 0.3) !important;
        background: rgba(25, 25, 30, 0.5) !important;
        box-shadow: 0 8px 30px rgba(139, 92, 246, 0.08) !important;
    }
    div[data-testid="stExpander"] details {
        border: none !important;
    }
    div[data-testid="stExpander"] summary {
        padding: 16px 20px !important;
        font-weight: 600 !important;
        color: #e2e8f0 !important;
    }
    div[data-testid="stExpander"] summary:hover {
        color: #c4b5fd !important;
    }

    /* ── Compact Emoji Feedback Buttons ── */
    .suggestion-actions {
        margin-top: -8px;
        margin-bottom: 24px;
        padding-left: 8px;
        display: flex;
        gap: 8px;
    }
    .suggestion-actions button {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 50% !important;
        width: 36px !important;
        height: 36px !important;
        min-width: 36px !important;
        max-width: 36px !important;
        padding: 0 !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 0.95rem !important;
        color: rgba(255, 255, 255, 0.7) !important;
        box-shadow: none !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .suggestion-actions button:hover {
        background: rgba(139, 92, 246, 0.15) !important;
        border-color: rgba(139, 92, 246, 0.4) !important;
        color: #ffffff !important;
        transform: scale(1.1) translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.2) !important;
    }
    .suggestion-actions button:active {
        transform: scale(0.95) !important;
    }

    /* ── Placeholder Card ── */
    .placeholder-card {
        border: 1px dashed rgba(255, 255, 255, 0.1);
        background: rgba(255, 255, 255, 0.01);
        border-radius: 20px;
        padding: 48px 32px;
        text-align: center;
        color: rgba(200, 200, 230, 0.4);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 280px;
        margin-top: 10px;
    }
    .placeholder-icon {
        font-size: 3rem;
        margin-bottom: 16px;
        opacity: 0.5;
    }
    .placeholder-text {
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 8px;
        color: rgba(200, 200, 230, 0.6);
    }
    .placeholder-desc {
        font-size: 0.9rem;
        max-width: 320px;
        line-height: 1.5;
    }
</style>
""", unsafe_allow_html=True)


# ─── Sidebar ───
with st.sidebar:
    st.markdown("### 🧭 Navigation")
    st.markdown("Use the tabs below to explore features.")
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    st.markdown("### ⚡ Quick Stats")
    try:
        hist = requests.get(f"{BASE_URL}/history", timeout=3).json()
        fb = requests.get(f"{BASE_URL}/feedback", timeout=3).json()
        hist_count = len(hist) if isinstance(hist, list) else 0
        fb_count = len(fb) if isinstance(fb, list) else 0
    except Exception:
        hist_count = 0
        fb_count = 0

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{hist_count}</div>
            <div class="metric-label">Sessions</div>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{fb_count}</div>
            <div class="metric-label">Feedbacks</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    st.markdown("### 🛠️ About")
    st.markdown(
        '<p style="color: rgba(200,200,230,0.5); font-size: 0.82rem; line-height: 1.6;">'
        'AI-powered networking assistant that generates smart, tailored conversation '
        'starters for professional events. Built with FastAPI + Streamlit.</p>',
        unsafe_allow_html=True
    )


# ─── Hero Banner ───
st.markdown("""
<div class="hero-banner">
    <h1>🤝 Networking Assistant</h1>
    <p class="hero-subtitle">
        Generate smart, AI-powered conversation starters tailored to your events and interests.
        Break the ice effortlessly. ✨
    </p>
</div>
""", unsafe_allow_html=True)


# ─── Tabs ───
tab1, tab2, tab3, tab4 = st.tabs([
    "🚀 Generate Starters",
    "🔍 Fact Check",
    "📜 History",
    "📊 Feedback"
])


# ━━━━━━━━━━━ TAB 1: Generate Conversation Starters ━━━━━━━━━━━
with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-header">🎯 Generate Conversation Starters</p>', unsafe_allow_html=True)

    event_description = st.text_area(
        "📝 Event Description",
        placeholder="e.g. AI for Sustainable Cities — a conference exploring how artificial intelligence can drive urban sustainability...",
        height=120
    )

    user_interests = st.text_input(
        "💡 Your Interests (comma-separated)",
        placeholder="e.g. climate change, urban planning, green energy"
    )

    generate_clicked = st.button("✨ Generate Starters", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if generate_clicked:
        if event_description and user_interests:
            payload = {
                "description": event_description,
                "interests": [i.strip() for i in user_interests.split(",")]
            }

            with st.spinner("🧠 AI is crafting your starters..."):
                try:
                    response = requests.post(f"{BASE_URL}/generate-conversation", json=payload, timeout=60)

                    if response.status_code == 200:
                        data = response.json()
                        st.session_state["topics"] = data["topics"]
                        st.session_state["suggestions"] = data["suggestions"]
                    else:
                        st.error("❌ Failed to generate conversation starters. Is the backend running?")
                except requests.exceptions.ConnectionError:
                    st.error("🔌 Cannot connect to backend. Please start the FastAPI server first.")
                except Exception as e:
                    st.error(f"⚠️ An unexpected error occurred: {e}")
        else:
            st.warning("⚠️ Please enter both an event description and your interests.")

    # Display results
    if "suggestions" in st.session_state and st.session_state["suggestions"]:
        st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

        # Topics
        st.markdown('<p class="section-header">🧠 Extracted Themes</p>', unsafe_allow_html=True)
        pills_html = ""
        for topic in st.session_state["topics"]:
            pills_html += f'<span class="topic-pill">{topic}</span>'
        st.markdown(f'<div style="margin-bottom: 20px;">{pills_html}</div>', unsafe_allow_html=True)

        # Suggestions
        st.markdown('<p class="section-header">💬 Conversation Starters</p>', unsafe_allow_html=True)
        for i, suggestion in enumerate(st.session_state["suggestions"]):
            st.markdown(
                f'<div class="starter-card">'
                f'<span class="starter-number">{i + 1}</span>'
                f'{suggestion}'
                f'</div>',
                unsafe_allow_html=True
            )

            col1, col2, col3 = st.columns([1, 1, 6])
            with col1:
                if st.button("👍", key=f"like_{i}"):
                    try:
                        resp = requests.post(
                            f"{BASE_URL}/feedback",
                            json={"suggestion": suggestion, "action": "thumbs_up"},
                            timeout=10
                        )
                        if resp.status_code == 200:
                            st.success("✅ Thanks for the feedback!")
                    except Exception:
                        st.error("Failed to submit feedback.")
            with col2:
                if st.button("👎", key=f"dislike_{i}"):
                    try:
                        resp = requests.post(
                            f"{BASE_URL}/feedback",
                            json={"suggestion": suggestion, "action": "thumbs_down"},
                            timeout=10
                        )
                        if resp.status_code == 200:
                            st.info("📝 Feedback noted.")
                    except Exception:
                        st.error("Failed to submit feedback.")


# ━━━━━━━━━━━ TAB 2: Fact Check ━━━━━━━━━━━
with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-header">🔍 Quick Fact-Check</p>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color: rgba(200,200,230,0.6); font-size: 0.9rem; margin-bottom: 16px;">'
        'Verify claims or explore topics before your networking event using Wikipedia summaries.</p>',
        unsafe_allow_html=True
    )

    query = st.text_input(
        "🔎 Topic to verify",
        placeholder="e.g. blockchain in healthcare, quantum computing, CRISPR..."
    )

    fact_clicked = st.button("🔬 Fact Check", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if fact_clicked:
        if query:
            with st.spinner("🔎 Looking up information..."):
                try:
                    response = requests.post(f"{BASE_URL}/fact-check", json={"query": query}, timeout=15)
                    if response.status_code == 200:
                        summary = response.json()["summary"]
                        st.markdown(
                            f'<div class="fact-result">✅ <strong>Result:</strong><br><br>{summary}</div>',
                            unsafe_allow_html=True
                        )
                    else:
                        st.error("❌ Fact-checking failed.")
                except requests.exceptions.ConnectionError:
                    st.error("🔌 Cannot connect to backend.")
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")
        else:
            st.warning("⚠️ Please enter a topic to fact-check.")


# ━━━━━━━━━━━ TAB 3: History ━━━━━━━━━━━
with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-header">📜 Conversation History</p>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color: rgba(200,200,230,0.6); font-size: 0.9rem; margin-bottom: 16px;">'
        'Review your recent conversation generation sessions.</p>',
        unsafe_allow_html=True
    )

    if st.button("🔄 Load History", use_container_width=True):
        try:
            response = requests.get(f"{BASE_URL}/history", timeout=10)
            if response.status_code == 200:
                history = response.json()
                if history:
                    st.session_state["history_data"] = history
                else:
                    st.info("📭 No history found yet. Generate some conversation starters first!")
            else:
                st.error("❌ Failed to load history.")
        except requests.exceptions.ConnectionError:
            st.error("🔌 Cannot connect to backend.")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

    if "history_data" in st.session_state and st.session_state["history_data"]:
        for item in reversed(st.session_state["history_data"]):
            # Support both old format and new format
            timestamp = item.get("created_at", item.get("timestamp", "N/A"))
            event_desc = item.get("event_description", item.get("description", "N/A"))
            themes = item.get("themes", item.get("topics", []))
            interests = item.get("interests", [])

            # Extract starters from nested or flat format
            starters = []
            content = item.get("content", {})
            if "conversation_starters" in content:
                starters = [s.get("starter", s) for s in content["conversation_starters"]]
            elif "suggestions" in item:
                starters = item["suggestions"]

            st.markdown(f"""
            <div class="history-card">
                <div class="history-timestamp">🕒 {timestamp}</div>
                <div class="history-event">📌 {event_desc}</div>
                <div class="history-detail">
                    <strong>Themes:</strong> {', '.join(themes) if themes else 'N/A'}<br>
                    <strong>Interests:</strong> {', '.join(interests) if interests else 'N/A'}
                </div>
            </div>
            """, unsafe_allow_html=True)

            if starters:
                for s in starters:
                    st.markdown(f'<div class="starter-card">💬 {s}</div>', unsafe_allow_html=True)


# ━━━━━━━━━━━ TAB 4: Feedback ━━━━━━━━━━━
with tab4:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-header">📊 Feedback History</p>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color: rgba(200,200,230,0.6); font-size: 0.9rem; margin-bottom: 16px;">'
        'See how you rated previous conversation starters.</p>',
        unsafe_allow_html=True
    )

    if st.button("🔄 Load Feedback", use_container_width=True):
        try:
            response = requests.get(f"{BASE_URL}/feedback", timeout=10)
            if response.status_code == 200:
                feedback_data = response.json()
                if feedback_data:
                    st.session_state["feedback_data"] = feedback_data
                else:
                    st.info("📭 No feedback submitted yet.")
            else:
                st.error("❌ Failed to load feedback.")
        except requests.exceptions.ConnectionError:
            st.error("🔌 Cannot connect to backend.")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

    if "feedback_data" in st.session_state and st.session_state["feedback_data"]:
        for item in reversed(st.session_state["feedback_data"]):
            # Support both old and new feedback format
            fb_type = item.get("feedback_type", item.get("feedback", ""))
            notes = item.get("notes", item.get("suggestion", ""))
            timestamp = item.get("submitted_at", item.get("timestamp", ""))

            if "up" in fb_type or fb_type == "like":
                icon = "👍"
                border_color = "rgba(34, 197, 94, 0.3)"
            else:
                icon = "👎"
                border_color = "rgba(239, 68, 68, 0.3)"

            st.markdown(f"""
            <div class="feedback-item" style="border-color: {border_color};">
                <span class="feedback-icon">{icon}</span>
                <span class="feedback-text">{notes}</span>
                <span class="feedback-time">🕒 {timestamp}</span>
            </div>
            """, unsafe_allow_html=True)
