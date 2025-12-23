import streamlit as st

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="VANTAGE // NEURAL LINK", page_icon="🌐", layout="wide")

# --- CYBER-DECK CSS ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Space+Mono&display=swap');
    
    /* 1. THE DEEP SPACE BACKGROUND */
    .stApp {
        background-color: #050505 !important;
        background-image: 
            radial-gradient(circle at 2px 2px, rgba(59, 130, 246, 0.15) 1px, transparent 0);
        background-size: 32px 32px;
    }

    /* 2. TEXT OVERRIDES */
    h1, h2, h3 { font-family: 'Syncopate', sans-serif !important; color: #ffffff !important; text-transform: uppercase; letter-spacing: 4px; }
    p, span, div { font-family: 'Space Mono', monospace !important; color: #a1a1aa !important; }

    /* 3. GLASS-MORPHIC PANELS */
    .cyber-panel {
        background: rgba(20, 20, 25, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        padding: 40px;
        border-radius: 2px;
        position: relative;
        overflow: hidden;
        transition: 0.5s ease;
    }
    .cyber-panel:hover {
        border-color: #3b82f6;
        box-shadow: 0 0 40px rgba(59, 130, 246, 0.2);
        transform: translateY(-5px);
    }
    .cyber-panel::before {
        content: ""; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: #3b82f6;
    }

    /* 4. NEON GLOW BUTTONS */
    .stButton > button {
        background: transparent !important;
        color: #3b82f6 !important;
        border: 1px solid #3b82f6 !important;
        border-radius: 0px !important;
        font-family: 'Syncopate' !important;
        font-size: 10px !important;
        letter-spacing: 3px !important;
        padding: 15px 30px !important;
        transition: 0.4s !important;
        text-transform: uppercase;
    }
    .stButton > button:hover {
        background: #3b82f6 !important;
        color: #ffffff !important;
        box-shadow: 0 0 30px #3b82f6;
    }

    /* 5. LIQUID NEON BAR */
    .liquid-bar {
        height: 2px;
        background: linear-gradient(90deg, transparent, #3b82f6, #8b5cf6, transparent);
        margin: 20px 0;
    }

    /* 6. HIDE NAV ELEMENTS */
    header, footer, #MainMenu { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION CONTROLLER ---
if 'page' not in st.session_state: st.session_state.page = 'HOME'

# CUSTOM SIDEBAR HUD
with st.sidebar:
    st.markdown("<h1>VANTAGE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 10px;'>PROTOCOL VERSION: 8.4.2</p>", unsafe_allow_html=True)
    st.markdown("<div class='liquid-bar'></div>", unsafe_allow_html=True)
    
    if st.button(">> 01_DASHBOARD"): st.session_state.page = 'HOME'
    if st.button(">> 02_LIVE_BOUNTIES"): st.session_state.page = 'BOUNTIES'
    if st.button(">> 03_MISSION_LOG"): st.session_state.page = 'MISSION'
    if st.button(">> 04_IDENTITY_NODE"): st.session_state.page = 'USER'
    
    st.markdown("<div style='margin-top: 100%;'></div>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 9px; opacity: 0.4;'>SECURE CONNECTION ESTABLISHED</p>", unsafe_allow_html=True)

# --- HOME INTERFACE ---
if st.session_state.page == 'HOME':
    st.markdown("<p style='color: #3b82f6;'>[ SYSTEM_STATUS: READY ]</p>", unsafe_allow_html=True)
    
    # Large Title
    st.markdown("""
        <div style='padding: 60px 0;'>
            <h1 style='font-size: 5rem; line-height: 1;'>THE FUTURE<br><span style='color: #3b82f6;'>OF WORK</span></h1>
            <p style='margin-top: 20px; font-size: 1.2rem; letter-spacing: 2px;'>BREAK THE RECURSIVE EXPERIENCE LOOP.</p>
        </div>
    """, unsafe_allow_html=True)

    # Content Grid
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class='cyber-panel'>
            <h3 style='color: #3b82f6;'>CORE_01</h3>
            <h2 style='font-size: 1.2rem;'>STEM / DATA</h2>
            <p style='font-size: 0.8rem; margin-top: 10px;'>Algorithmic testing, Python automation, and data sanitization for AI nodes.</p>
        </div>""", unsafe_allow_html=True)
        st.button("INITIALIZE SCTR_01", key="btn1")

    with col2:
        st.markdown("""<div class='cyber-panel'>
            <h3 style='color: #8b5cf6;'>CORE_02</h3>
            <h2 style='font-size: 1.2rem;'>GROWTH</h2>
            <p style='font-size: 0.8rem; margin-top: 10px;'>SEO architectural mapping, brand logic, and social engineering loops.</p>
        </div>""", unsafe_allow_html=True)
        st.button("INITIALIZE SCTR_02", key="btn2")

    with col3:
        st.markdown("""<div class='cyber-panel'>
            <h3 style='color: #ec4899;'>CORE_03</h3>
            <h2 style='font-size: 1.2rem;'>BIZ_INTEL</h2>
            <p style='font-size: 0.8rem; margin-top: 10px;'>Venture research, lead-gen architecture, and market intelligence.</p>
        </div>""", unsafe_allow_html=True)
        st.button("INITIALIZE SCTR_03", key="btn3")

# --- BOUNTIES INTERFACE ---
elif st.session_state.page == 'BOUNTIES':
    st.markdown("<h1>LIVE_BOUNTIES</h1>", unsafe_allow_html=True)
    st.text_input("QUERY DATABASE_")
    
    st.markdown("""
        <div class='cyber-panel' style='margin-top: 20px;'>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div>
                    <h2 style='font-size: 1.5rem; margin: 0;'>DATA_CLEAN_04</h2>
                    <p>NODE: TECH_FLOW_AI // SKILL: PYTHON</p>
                </div>
                <div style='text-align: right;'>
                    <h1 style='color: #3b82f6; font-size: 2rem; margin: 0;'>150.00</h1>
                    <p>USDT_REWARD</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("CLAIM_TASK_UPLINK")

# --- MISSION INTERFACE ---
elif st.session_state.page == 'MISSION':
    st.markdown("<h1>MISSION_LOG</h1>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""<div style='border: 1px solid #3b82f6; padding: 10px;'>""", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1614728263952-84ea256f9679?auto=format&fit=crop&q=80&w=1000")
        st.markdown("</div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("""
            <h3>PROTOCOL_VANTAGE</h3>
            <p style='font-size: 1.1rem;'>The current economy is built on a "Proof of Network" model. If you don't know someone, you don't get in.</p>
            <br>
            <p style='font-size: 1.1rem; color: #ffffff;'>We are replacing this with "Proof of Skill."</p>
            <br>
            <p>By atomizing work into Bounties, we allow students from any background to bypass the resume screen and prove their worth through hard deliverables.</p>
        """, unsafe_allow_html=True)

# --- USER INTERFACE ---
elif st.session_state.page == 'USER':
    st.markdown("<h1>IDENTITY_NODE</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 2])
    with c1:
        st.markdown("""
            <div class='cyber-panel' style='text-align: center;'>
                <div style='width: 100px; height: 100px; background: #3b82f6; border-radius: 50%; margin: 0 auto; box-shadow: 0 0 30px #3b82f6;'></div>
                <h2 style='margin-top: 20px;'>ALEX_RIVERA</h2>
                <p>OAKLAND_CALIFORNIA</p>
                <div style='background: #3b82f6; color: white; padding: 5px; margin-top: 15px;'>
                    <span style='color: white !important;'>LVL: ELITE_10</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='cyber-panel'><h3>VERIFIED_LEDGER</h3>", unsafe_allow_html=True)
        st.markdown("<p style='border-bottom: 1px solid rgba(255,255,255,0.1); padding: 10px 0;'>>> PYTHON_SCRPT_01 // VERIFIED_BY_STARTUP_X</p>", unsafe_allow_html=True)
        st.markdown("<p style='border-bottom: 1px solid rgba(255,255,255,0.1); padding: 10px 0;'>>> SEO_AUDIT_V2 // VERIFIED_BY_GLOBAL_CO</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.button("GENERATE_PORTFOLIO_LINK")
