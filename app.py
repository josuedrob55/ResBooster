import streamlit as st

# --- CORE CONFIG ---
st.set_page_config(page_title="VANTAGE // PROTOCOL", page_icon="📡", layout="wide")

# --- THE "OUT OF THIS WORLD" UI ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@100;400&display=swap');
    
    /* 1. THE VOID (WHITE EDITION) */
    .stApp {
        background: #ffffff;
        background-image: 
            linear-gradient(rgba(0,0,0,0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,0,0,0.05) 1px, transparent 1px);
        background-size: 100px 100px; /* Large architectural grid */
    }

    /* 2. NEON SCANNERS (The Futuristic Detail) */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 2px;
        background: linear-gradient(90deg, transparent, #3b82f6, transparent);
        animation: scan 4s linear infinite;
        z-index: 999;
    }
    @keyframes scan { 0% { top: 0%; } 100% { top: 100%; } }

    /* 3. TYPOGRAPHY */
    h1, h2, h3 { font-family: 'Orbitron', sans-serif !important; letter-spacing: 5px !important; text-transform: uppercase; }
    p, div, span { font-family: 'JetBrains Mono', monospace !important; color: #000000 !important; }

    /* 4. FLOATING GLASS CARDS */
    .glass-card {
        background: rgba(255, 255, 255, 0.01);
        border: 1px solid #000;
        padding: 40px;
        position: relative;
        transition: 0.5s;
        overflow: hidden;
    }
    .glass-card::after {
        content: "EXT-0042";
        position: absolute;
        bottom: 5px; right: 5px; font-size: 8px; opacity: 0.3;
    }
    .glass-card:hover {
        background: #000;
        color: #fff !important;
        box-shadow: 0 0 50px rgba(59, 130, 246, 0.3);
    }
    .glass-card:hover * { color: #fff !important; }

    /* 5. CYBER BUTTONS */
    .stButton > button {
        border-radius: 0px !important;
        border: 1px solid #000 !important;
        background: transparent !important;
        color: #000 !important;
        font-family: 'Orbitron' !important;
        font-size: 12px !important;
        letter-spacing: 3px !important;
        padding: 20px !important;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background: #3b82f6 !important;
        border-color: #3b82f6 !important;
        color: #fff !important;
        box-shadow: 0 0 20px #3b82f6;
    }

    /* 6. HIDE STREAMLIT JUNK */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- THE COMMAND NAV ---
if 'page' not in st.session_state: st.session_state.page = 'CORE'

# Top HUD (Heads Up Display)
st.markdown("<p style='text-align:center; font-size:10px; letter-spacing:10px;'>VANTAGE // SYSTEM_STATUS: ONLINE // ENCRYPTED_CONNECTION</p>", unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns([2,1,1,1,1])
with c1: st.markdown("<h1 style='margin:0;'>VNTG_</h1>", unsafe_allow_html=True)
with c2: 
    if st.button("[ 01.CORE ]"): st.session_state.page = 'CORE'
with c3: 
    if st.button("[ 02.LINK ]"): st.session_state.page = 'BOUNTIES'
with c4: 
    if st.button("[ 03.DATA ]"): st.session_state.page = 'MISSION'
with c5: 
    if st.button("[ 04.USER ]"): st.session_state.page = 'USER'

st.markdown("<div style='height:1px; background:black; width:100%; margin:20px 0;'></div>", unsafe_allow_html=True)

# --- CORE INTERFACE (HOME) ---
if st.session_state.page == 'CORE':
    st.markdown("<p style='font-size:12px;'>>> INITIALIZING NEURAL UPLINK...</p>", unsafe_allow_html=True)
    
    # Hero
    st.markdown("""
        <div style='padding:100px 0; text-align:center;'>
            <h1 style='font-size:5rem; line-height:0.8;'>RECODE<br>YOUR<br>CAREER</h1>
            <p style='margin-top:20px; letter-spacing:5px;'>SKILLS ARE THE ONLY CURRENCY THAT MATTERS.</p>
        </div>
    """, unsafe_allow_html=True)

    # Grid Sectors
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class='glass-card'>
            <h2>SCTR_01</h2>
            <p>STEM / QUANTUM DATA / AUTOMATION</p>
            <p style='font-size:10px; margin-top:20px;'>>> ENCRYPTED TASKS AVAILABLE</p>
        </div>""", unsafe_allow_html=True)
        st.button("ENTER SCTR_01", key="s1")
    with col2:
        st.markdown("""<div class='glass-card'>
            <h2>SCTR_02</h2>
            <p>MARKETING / GROWTH / PSYCHOLOGY</p>
            <p style='font-size:10px; margin-top:20px;'>>> OPEN ENGINE PROTOCOLS</p>
        </div>""", unsafe_allow_html=True)
        st.button("ENTER SCTR_02", key="s2")
    with col3:
        st.markdown("""<div class='glass-card'>
            <h2>SCTR_03</h2>
            <p>BIZ-OPS / INTELLIGENCE / RESEARCH</p>
            <p style='font-size:10px; margin-top:20px;'>>> SYSTEM CLEARANCE GRANTED</p>
        </div>""", unsafe_allow_html=True)
        st.button("ENTER SCTR_03", key="s3")

# --- LINK INTERFACE (BOUNTIES) ---
elif st.session_state.page == 'BOUNTIES':
    st.markdown("<h1>ACTIVE_BOUNTIES</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:10px;'>FILTERING BY SKILL_TREE...</p>", unsafe_allow_html=True)
    
    st.text_input("QUERY_DATABASE")
    
    st.markdown("""
        <div style='border:1px solid black; padding:40px; margin-top:20px;'>
            <div style='display:flex; justify-content:space-between;'>
                <div>
                    <h2 style='margin:0;'>LEAD_GEN_ARCH</h2>
                    <p>COMPANY: TECH_FLOW // REWARD: 150_CREDITS</p>
                </div>
                <div style='text-align:right;'>
                    <p>04:59:59</p>
                    <p style='font-size:8px;'>EST_TIME_TO_COMPLETE</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("DOWNLOAD_BRIEF_UPLINK")

# --- DATA INTERFACE (MISSION) ---
elif st.session_state.page == 'MISSION':
    st.markdown("<h1>OUR_PROTOCOL</h1>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1000")
    with col_b:
        st.markdown("""
            <h3>THE PROBLEM</h3>
            <p>Legacy systems require "Experience" to grant "Experience." This is a recursive loop that excludes underrepresented talent.</p>
            <br>
            <h3>THE SOLUTION</h3>
            <p>Vantage bypasses the resume. We provide technical Bounties. Complete the work, earn the credits, build the verified profile.</p>
            <br>
            <h3>THE FUTURE</h3>
            <p>A world where your ability to solve a problem is the only thing that opens the door.</p>
        """, unsafe_allow_html=True)

# --- USER INTERFACE (PORTFOLIO) ---
elif st.session_state.page == 'USER':
    st.markdown("<h1>USER_PROFILE</h1>", unsafe_allow_html=True)
    c_p1, c_p2 = st.columns([1, 2])
    with c_p1:
        st.markdown("""
            <div style='border:5px solid black; padding:40px; text-align:center;'>
                <h1 style='font-size:10rem; margin:0;'>A</h1>
                <h3>ALEX_RIVERA</h3>
                <p style='background:black; color:white !important;'>RANK: ELITE_10%</p>
            </div>
        """, unsafe_allow_html=True)
    with c_p2:
        st.markdown("<h3>VERIFIED_LEDGER</h3>", unsafe_allow_html=True)
        st.markdown("""
            <div style='border-bottom:1px solid black; padding:20px 0;'>
                <p><b>TASK:</b> DATA_CLEAN_V4 // <b>NODE:</b> AI_LABS // <b>STATUS:</b> VERIFIED</p>
            </div>
            <div style='border-bottom:1px solid black; padding:20px 0;'>
                <p><b>TASK:</b> SEO_MAP_09 // <b>NODE:</b> BAKERY_CO // <b>STATUS:</b> VERIFIED</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("EXPORT_PORTFOLIO_KEY")
