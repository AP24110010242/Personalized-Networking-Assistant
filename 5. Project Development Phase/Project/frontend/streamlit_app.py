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
        color: rgba(255, 255, 255, 0.9) !important;
    }

    /* ── Glass Card ── */
    .glass-card {
        background: rgba(20, 20, 25, 0.6) !important;
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        padding: 32px;
        margin-bottom: 24px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4), 
                    inset 0 1px 0 0 rgba(255, 255, 255, 0.03);
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
            rgba(255, 255, 255, 0.05) 50%,
            rgba(255, 255, 255, 0.01) 70%,
            rgba(255, 255, 255, 0) 100%
        );
        transform: skewX(-25deg);
        pointer-events: none;
    }

    .glass-card:hover {
        transform: translateY(-2px);
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 16px 48px rgba(99, 102, 241, 0.15), 
                    inset 0 1px 0 0 rgba(255, 255, 255, 0.05);
    }

    .glass-card:hover::before {
        left: 150%;
        transition: left 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* ── Hero Banner ── */
    .hero-banner {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.08) 0%, rgba(168, 85, 247, 0.08) 50%, rgba(6, 182, 212, 0.08) 100%);
        backdrop-filter: blur(30px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 40px 32px;
        margin-bottom: 32px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
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
            rgba(255, 255, 255, 0.05) 50%,
            rgba(255, 255, 255, 0.01) 70%,
            rgba(255, 255, 255, 0) 100%
        );
        transform: skewX(-25deg);
        pointer-events: none;
    }

    .hero-banner:hover {
        transform: translateY(-1px);
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 16px 48px rgba(99, 102, 241, 0.1);
    }

    .hero-banner:hover::before {
        left: 150%;
        transition: left 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .hero-banner h1 {
        font-size: 2.6rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #a78bfa, #e879f9, #22d3ee);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 12px !important;
        letter-spacing: -0.5px;
        position: relative;
        z-index: 2;
    }

    .hero-subtitle {
        color: rgba(200, 200, 230, 0.7);
        font-size: 1.1rem;
        font-weight: 400;
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
        color: #e2e8f0 !important;
        margin-bottom: 16px !important;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* ── Starter Card ── */
    .starter-card {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 20px 24px;
        margin-bottom: 12px;
        color: #ffffff;
        font-size: 1rem;
        line-height: 1.6;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .starter-card:hover {
        background: rgba(255, 255, 255, 0.05) !important;
        border-color: rgba(139, 92, 246, 0.3);
        transform: translateX(4px);
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.08);
    }

    .starter-number {
        display: inline-block;
        background: linear-gradient(135deg, #8b5cf6, #ec4899);
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
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(236, 72, 153, 0.15));
        border: 1px solid rgba(139, 92, 246, 0.4);
        border-radius: 30px;
        padding: 6px 18px;
        margin: 4px 6px 4px 0;
        color: #c4b5fd;
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 0.3px;
    }

    /* ── History Card (Fallback) ── */
    .history-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 16px;
        transition: all 0.3s ease;
    }

    .history-card:hover {
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(255, 255, 255, 0.1);
    }

    .history-timestamp {
        color: rgba(200, 200, 230, 0.4);
        font-size: 0.8rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .history-event {
        color: #ffffff;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 10px;
    }

    .history-detail {
        color: rgba(200, 200, 230, 0.7);
        font-size: 0.9rem;
    }

    /* ── Feedback Pill ── */
    .feedback-item {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
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
        color: #e2e8f0;
        font-size: 0.95rem;
        flex: 1;
    }

    .feedback-time {
        color: rgba(200, 200, 230, 0.4);
        font-size: 0.75rem;
    }

    /* ── Fact Check Result ── */
    .fact-result {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(4, 120, 87, 0.15));
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 16px;
        padding: 24px;
        color: #a7f3d0;
        line-height: 1.7;
        font-size: 0.95rem;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 10px 28px !important;
        font-weight: 600 !important;
        font-family: 'Outfit', 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.3px;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #4f46e5, #6366f1) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.4) !important;
    }

    .stButton > button:active {
        transform: translateY(0px) !important;
    }

    /* ── Text Inputs (CRITICAL VISIBILITY FIX) ── */
    .stTextArea textarea, .stTextInput input, div[data-baseweb="input"] input, div[data-baseweb="textarea"] textarea {
        background: #101014 !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 14px !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        font-family: 'Outfit', 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        padding: 12px 16px !important;
        transition: all 0.3s ease !important;
        box-shadow: inset 0 1px 2px rgba(0,0,0,0.2) !important;
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
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.05), transparent);
        margin: 32px 0;
        border: none;
    }

    /* ── Tabs styling ── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 16px;
        padding: 6px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 12px !important;
        color: rgba(200, 200, 230, 0.6) !important;
        font-weight: 600 !important;
        font-family: 'Outfit', 'Inter', sans-serif !important;
        padding: 10px 24px !important;
        transition: all 0.2s ease !important;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: #ffffff !important;
        background: rgba(255, 255, 255, 0.05) !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(168, 85, 247, 0.2)) !important;
        color: #c4b5fd !important;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.15) !important;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        display: none;
    }

    /* ── Alert boxes ── */
    .stAlert {
        border-radius: 12px !important;
        background-color: rgba(20, 20, 25, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    /* ── Spinner ── */
    .stSpinner > div {
        border-top-color: #8b5cf6 !important;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(139, 92, 246, 0.2); border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(139, 92, 246, 0.4); }

    /* ── Hide Streamlit branding ── */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    /* ── Metric cards ── */
    .metric-card {
        background: rgba(255, 255, 255, 0.04) !important;
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px 24px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
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
        border-radius: 18px !important;
        margin-bottom: 12px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2) !important;
        overflow: hidden !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
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
    col_history, col_workspace = st.columns([5, 7], gap="large")
    
    # ─── LEFT COLUMN: Chat Results / History ───
    with col_history:
        st.markdown('<p class="section-header">📜 Chat Results</p>', unsafe_allow_html=True)
        st.markdown('<span style="color: #64748b; font-size: 0.8rem; font-weight: 700; letter-spacing: 1px; display: block; margin-bottom: 12px; text-transform: uppercase;">Recent Sessions</span>', unsafe_allow_html=True)
        
        try:
            response = requests.get(f"{BASE_URL}/history", timeout=5)
            if response.status_code == 200:
                history = response.json()
                if history:
                    for idx, item in enumerate(reversed(history[-5:])): # Show last 5
                        timestamp = item.get("created_at", item.get("timestamp", "N/A"))
                        event_desc = item.get("event_description", item.get("description", "N/A"))
                        themes = item.get("themes", item.get("topics", []))
                        interests = item.get("interests", [])
                        suggestions = item.get("suggestions", [])
                        if not suggestions and "content" in item:
                            suggestions = [s.get("starter", s) if isinstance(s, dict) else s for s in item["content"].get("conversation_starters", [])]
                        
                        st.markdown(f"""
                        <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 16px; padding: 16px; margin-bottom: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
                            <div style="color: rgba(200, 200, 230, 0.4); font-size: 0.75rem; font-weight: 600; margin-bottom: 4px;">🕒 {timestamp}</div>
                            <div style="color: #ffffff; font-size: 0.9rem; font-weight: 600; margin-bottom: 6px; line-height: 1.4;">📌 {event_desc[:55]}...</div>
                            <div style="color: rgba(200, 200, 230, 0.7); font-size: 0.8rem; line-height: 1.4;">
                                <strong>Themes:</strong> {', '.join(themes[:2]) if themes else 'None'}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button("📂 Open Session", key=f"load_session_{idx}", use_container_width=True):
                            st.session_state["topics"] = themes
                            st.session_state["suggestions"] = suggestions
                            st.session_state["loaded_desc"] = event_desc
                            st.session_state["loaded_interests"] = ", ".join(interests)
                            st.rerun()
                else:
                    st.info("📭 No past chats found.")
            else:
                st.error("Failed to load history.")
        except Exception:
            st.error("🔌 Backend server not reachable.")

    # ─── RIGHT COLUMN: Active Workspace ───
    with col_workspace:
        has_active = "suggestions" in st.session_state and st.session_state["suggestions"]
        
        st.markdown('<p class="section-header">🤖 Active Assistant</p>', unsafe_allow_html=True)
        
        # Display suggestions list at the top (similar to active bubble chat in reference)
        if has_active:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown('<span style="color: #4f46e5; font-size: 0.8rem; font-weight: 700; letter-spacing: 1px; display: block; margin-bottom: 8px; text-transform: uppercase;">Extracted Themes</span>', unsafe_allow_html=True)
            pills_html = ""
            for topic in st.session_state["topics"]:
                pills_html += f'<span class="topic-pill">{topic}</span>'
            st.markdown(f'<div style="margin-bottom: 24px;">{pills_html}</div>', unsafe_allow_html=True)
            
            st.markdown('<span style="color: #4f46e5; font-size: 0.8rem; font-weight: 700; letter-spacing: 1px; display: block; margin-bottom: 12px; text-transform: uppercase;">Conversation Starters</span>', unsafe_allow_html=True)
            for i, suggestion in enumerate(st.session_state["suggestions"]):
                st.markdown(
                    f'<div class="starter-card">'
                    f'<span class="starter-number">{i + 1}</span>'
                    f'{suggestion}'
                    f'</div>',
                    unsafe_allow_html=True
                )
                
                st.markdown('<div class="suggestion-actions">', unsafe_allow_html=True)
                col1, col2, col3 = st.columns([1.5, 1.5, 9])
                with col1:
                    if st.button("👍", key=f"like_{i}"):
                        try:
                            resp = requests.post(
                                f"{BASE_URL}/feedback",
                                json={"suggestion": suggestion, "action": "thumbs_up"},
                                timeout=10
                            )
                            if resp.status_code == 200:
                                st.success("Saved!")
                        except Exception:
                            st.error("Error.")
                with col2:
                    if st.button("👎", key=f"dislike_{i}"):
                        try:
                            resp = requests.post(
                                f"{BASE_URL}/feedback",
                                json={"suggestion": suggestion, "action": "thumbs_down"},
                                timeout=10
                            )
                            if resp.status_code == 200:
                                st.info("Noted.")
                        except Exception:
                            st.error("Error.")
                st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            # Styled tablet placeholder
            st.markdown(f"""
            <div class="placeholder-card">
                <div class="placeholder-icon">🤖</div>
                <div class="placeholder-text">Hi! How can I help you?</div>
                <div class="placeholder-desc">
                    Enter event settings below to generate tailored starters, or select a past session from the left column.
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        # Settings/inputs form at the bottom (matching bottom input bar in reference)
        st.markdown('<div class="glass-card" style="margin-top: 16px;">', unsafe_allow_html=True)
        st.markdown('<span style="color: #4f46e5; font-size: 0.8rem; font-weight: 700; letter-spacing: 1px; display: block; margin-bottom: 8px; text-transform: uppercase;">Configure Chat</span>', unsafe_allow_html=True)
        
        default_desc = st.session_state.get("loaded_desc", "")
        default_interests = st.session_state.get("loaded_interests", "")
        
        event_description = st.text_area(
            "📝 Event Description",
            value=default_desc,
            placeholder="e.g. AI for Sustainable Cities — a conference exploring urban sustainability...",
            height=100,
            key="active_event_description"
        )

        user_interests = st.text_input(
            "💡 Your Interests (comma-separated)",
            value=default_interests,
            placeholder="e.g. climate change, urban planning",
            key="active_user_interests"
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
                            st.session_state["loaded_desc"] = event_description
                            st.session_state["loaded_interests"] = user_interests
                            st.rerun()
                        else:
                            st.error("❌ Failed to generate conversation starters.")
                    except requests.exceptions.ConnectionError:
                        st.error("🔌 Cannot connect to backend.")
                    except Exception as e:
                        st.error(f"⚠️ Error: {e}")
            else:
                st.warning("⚠️ Please fill in both fields.")


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

            expander_title = f"🕒 {timestamp} — {event_desc[:45]}..." if len(event_desc) > 45 else f"🕒 {timestamp} — {event_desc}"
            
            with st.expander(expander_title, expanded=False):
                st.markdown(f"""
                <div style="padding: 4px 0;">
                    <p style="color: #c4b5fd; font-weight: 600; margin-bottom: 8px; font-size: 0.95rem;">📌 Event Description</p>
                    <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px;">{event_desc}</p>
                    <div style="background: rgba(255,255,255,0.02); border-radius: 12px; padding: 16px; border: 1px solid rgba(255,255,255,0.04); margin-bottom: 20px;">
                        <span style="color: rgba(200, 200, 230, 0.6); font-size: 0.85rem; display: block; margin-bottom: 4px;">BRAINSTORMED THEMES</span>
                        <span style="color: #e2e8f0; font-weight: 500; font-size: 0.9rem; display: block;">{', '.join(themes) if themes else 'None'}</span>
                        <span style="color: rgba(200, 200, 230, 0.6); font-size: 0.85rem; display: block; margin-top: 12px; margin-bottom: 4px;">YOUR INTERESTS</span>
                        <span style="color: #e2e8f0; font-weight: 500; font-size: 0.9rem; display: block;">{', '.join(interests) if interests else 'None'}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if starters:
                    st.markdown('<p style="color: #c4b5fd; font-weight: 600; margin-bottom: 12px; font-size: 0.95rem;">💬 AI-Generated Starters</p>', unsafe_allow_html=True)
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
