import streamlit as st
import time

# --- SYSTEM CONFIGURATION ---
st.set_page_config(
    page_title="VANTAGE // NEURAL_LINK_V8", 
    page_icon="🧬", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- THE "HYPER-DRIVE" CSS ENGINE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=JetBrains+Mono:wght@100;400;700&family=Rajdhani:wght@300;500;700&display=swap');
    
    /* 1. TOTAL DARKNESS OVERRIDE */
    .stApp, .main, .block-container {
        background-color: #020202 !important;
        background-image: 
            radial-gradient(circle at 2px 2px, rgba(0, 255, 255, 0.05) 1px, transparent 0);
        background-size: 30px 30px;
        color: #e2e8f0 !important;
    }

    /* 2. ANIMATED SCANNING HUD */
    .stApp::after {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 3px;
        background: rgba(0, 255, 255, 0.2);
        box-shadow: 0 0 15px #00ffff;
        animation: scanline 8s linear infinite;
        z-index: 9999;
        pointer-events: none;
    }
    @keyframes scanline {
        0% { top: 0%; }
        100% { top: 100%; }
    }

    /* 3. TYPOGRAPHY HIERARCHY */
    h1 {
        font-family: 'Orbitron', sans-serif !important;
        color: #00ffff !important;
        text-shadow: 0 0 20px rgba(0, 255, 255, 0.6);
        letter-spacing: 8px !important;
        text-transform: uppercase;
        font-weight: 900 !important;
    }
    h2, h3 {
        font-family: 'Rajdhani', sans-serif !important;
        color: #ff00ff !important;
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    p, div, label {
        font-family: 'JetBrains Mono', monospace !important;
        color: #cbd5e1 !important;
    }

    /* 4. CYBER-CARD ARCHITECTURE */
    .cyber-card {
        background: rgba(10, 10, 15, 0.9) !important;
        border: 1px solid rgba(0, 255, 255, 0.3);
        padding: 30px;
        position: relative;
        transition: 0.5s;
        margin-bottom: 25px;
        clip-path: polygon(0 0, 95% 0, 100% 5%, 100% 100%, 5% 100%, 0 95%);
    }
    .cyber-card:hover {
        border-color: #ff00ff;
        box-shadow: 0 0 30px rgba(255, 0, 255, 0.3);
        transform: translateY(-5px);
    }
    .cyber-card::before {
        content: "STATUS: ACTIVE";
        position: absolute;
        top: 5px; right: 15px;
        font-size: 8px;
        color: #00ffff;
        letter-spacing: 1px;
    }

    /* 5. NEON BUTTON INTERFACE */
    .stButton > button {
        width: 100% !important;
        background: transparent !important;
        color: #00ffff !important;
        border: 1px solid #00ffff !important;
        font-family: 'Orbitron' !important;
        text-transform: uppercase;
        letter-spacing: 4px;
        padding: 20px !important;
        border-radius: 0px !important;
        transition: 0.3s;
        margin-top: 10px;
    }
    .stButton > button:hover {
        background: rgba(0, 255, 255, 0.1) !important;
        box-shadow: 0 0 20px #00ffff, inset 0 0 10px #00ffff;
        color: #ffffff !important;
    }

    /* 6. SIDEBAR CUSTOMIZATION */
    section[data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 1px solid #333;
        width: 300px !important;
    }
    section[data-testid="stSidebar"] h1 {
        font-size: 20px !important;
        color: #ff00ff !important;
    }

    /* 7. PROGRESS BARS (Neural Loading) */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00ffff , #ff00ff) !important;
    }

    /* HIDE DEFAULT ELEMENTS */
    header, footer, #MainMenu { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION CONTROLLER ---
if 'terminal_page' not in st.session_state:
    st.session_state.terminal_page = 'COMMAND_CENTER'

def switch_terminal(target):
    st.session_state.terminal_page = target

# --- SIDEBAR HUD ---
with st.sidebar:
    st.markdown("<h1>VANTAGE // PROTOCOL</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 10px; color: #555;'>BUILD_VER: 0.8.4-ALPHA</p>", unsafe_allow_html=True)
    st.divider()
    
    st.button(">> [01] COMMAND_CENTER", on_click=switch_terminal, args=('COMMAND_CENTER',))
    st.button(">> [02] BOUNTY_BOARD", on_click=switch_terminal, args=('BOUNTY_BOARD',))
    st.button(">> [03] THE_MANIFESTO", on_click=switch_terminal, args=('MANIFESTO',))
    st.button(">> [04] NEURAL_PROFILE", on_click=switch_terminal, args=('PROFILE',))
    
    st.divider()
    st.markdown("""
        <div style='background: rgba(255,0,0,0.1); padding: 15px; border: 1px solid red;'>
            <p style='color: red !important; font-size: 10px; margin: 0;'><b>WARNING:</b> UNAUTHORIZED ACCESS TO CORE DATA WILL TRIGGER LOCKOUT.</p>
        </div>
    """, unsafe_allow_html=True)

# --- TERMINAL PAGE: COMMAND_CENTER (HOME) ---
if st.session_state.terminal_page == 'COMMAND_CENTER':
    st.markdown("<p style='color: #00ffff;'>>> INITIALIZING_SYSTEM_BOOT...</p>", unsafe_allow_html=True)
    
    # Hero Visual
    st.markdown("""
        <div style='text-align: center; padding: 60px 0;'>
            <h1 style='font-size: 6rem; margin: 0;'>VANTAGE</h1>
            <p style='letter-spacing: 12px; color: #ff00ff !important; font-weight: bold;'>REWRITING THE CAREER ALGORITHM</p>
        </div>
    """, unsafe_allow_html=True)

    # Sector Layout
    st.markdown("### >> SELECT_OPERATIONAL_SECTOR")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class='cyber-card'>
            <h2 style='color: #00ffff !important;'>SECTOR_01: STEM</h2>
            <p>PYTHON_UPLINK // DATA_CLEAN // ALGO_QA</p>
            <p style='font-size: 12px; margin-top: 15px;'>Tasks: 14 Active</p>
            <p style='font-size: 12px;'>Difficulty: HIGH</p>
        </div>""", unsafe_allow_html=True)
        st.button("ENTER_STEM_GRID", key="e1")

    with col2:
        st.markdown("""<div class='cyber-card'>
            <h2 style='color: #ff00ff !important;'>SECTOR_02: GROWTH</h2>
            <p>SEO_ARCH // SOCIAL_ENG // BRAND_LOGIC</p>
            <p style='font-size: 12px; margin-top: 15px;'>Tasks: 09 Active</p>
            <p style='font-size: 12px;'>Difficulty: MEDIUM</p>
        </div>""", unsafe_allow_html=True)
        st.button("ENTER_GROWTH_GRID", key="e2")

    with col3:
        st.markdown("""<div class='cyber-card'>
            <h2 style='color: #f59e0b !important;'>SECTOR_03: INTEL</h2>
            <p>BIZ_RESEARCH // LEAD_GEN // MARKET_AUDIT</p>
            <p style='font-size: 12px; margin-top: 15px;'>Tasks: 22 Active</p>
            <p style='font-size: 12px;'>Difficulty: STABLE</p>
        </div>""", unsafe_allow_html=True)
        st.button("ENTER_INTEL_GRID", key="e3")

# --- TERMINAL PAGE: BOUNTY_BOARD ---
elif st.session_state.terminal_page == 'BOUNTY_BOARD':
    st.markdown("<h1>AVAILABLE_BOUNTIES</h1>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.text_input("QUERY_BOUNTY_DATABASE_")
    with c2:
        st.selectbox("SORT_BY", ["REWARD_HIGH", "EXPIRY_SOON", "SKILL_MATCH"])

    # Detailed Bounty Card 1
    st.markdown("""
        <div class='cyber-card' style='border-left: 5px solid #00ffff;'>
            <div style='display: flex; justify-content: space-between;'>
                <div>
                    <h2 style='margin:0;'>NEURAL_DATA_SANitization</h2>
                    <p style='color: #00ffff !important;'>CLIENT: NEXUS_AI_CORP // DEADLINE: 48H</p>
                    <p style='font-size: 14px;'>Cleanse 5,000 nodes of unstructured training data. Python knowledge required.</p>
                </div>
                <div style='text-align: right;'>
                    <h1 style='color: #00ffff !important; margin: 0;'>$250</h1>
                    <p style='font-size: 10px;'>CREDIT_PAYOUT</p>
                    <span style='background: #00ffff; color: black; padding: 2px 5px; font-size: 10px;'>VERIFIED_TASK</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("CLAIM_BOUNTY_01")

    # Detailed Bounty Card 2
    st.markdown("""
        <div class='cyber-card' style='border-left: 5px solid #ff00ff;'>
            <div style='display: flex; justify-content: space-between;'>
                <div>
                    <h2 style='margin:0;'>SEO_ARCHITECT_RECON</h2>
                    <p style='color: #ff00ff !important;'>CLIENT: GHOST_MEDIA // DEADLINE: 72H</p>
                    <p style='font-size: 14px;'>Map competitor keyword clusters and build a 30-day growth engine.</p>
                </div>
                <div style='text-align: right;'>
                    <h1 style='color: #ff00ff !important; margin: 0;'>$180</h1>
                    <p style='font-size: 10px;'>CREDIT_PAYOUT</p>
                    <span style='background: #ff00ff; color: black; padding: 2px 5px; font-size: 10px;'>VERIFIED_TASK</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("CLAIM_BOUNTY_02")

# --- TERMINAL PAGE: MANIFESTO ---
elif st.session_state.terminal_page == 'MANIFESTO':
    st.markdown("<h1 style='text-align:center;'>THE_PROTOCOL</h1>", unsafe_allow_html=True)
    
    col_a, col_b = st.columns([1, 1])
    with col_a:
        st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=1000")
    with col_b:
        st.markdown("""
            <h3>>> THE_PROBLEM</h3>
            <p>Legacy career paths are gated by "The Network." If you don't have the connections, you don't get the experience. This creates a recursive loop of exclusion.</p>
            <br>
            <h3>>> THE_VANTAGE_SOLUTION</h3>
            <p>We atomize professional work into Bounties. We allow the world's best talent to prove their worth through hard deliverables—not resumes.</p>
            <br>
            <h3>>> THE_FUTURE</h3>
            <p>A decentralized meritocracy where your <b>Verified Proof of Work</b> is the only currency you need to enter the room.</p>
            <br>
            <div style='border: 1px solid #00ffff; padding: 20px;'>
                <p style='margin:0; color: #00ffff !important;'><b>// NO RÉSUMÉS // NO REFERRALS // JUST SKILL.</b></p>
            </div>
        """, unsafe_allow_html=True)

# --- TERMINAL PAGE: PROFILE ---
elif st.session_state.terminal_page == 'PROFILE':
    st.markdown("<h1>NEURAL_LINK_IDENTITY</h1>", unsafe_allow_html=True)
    
    c_p1, c_p2 = st.columns([1, 2])
    with c_p1:
        st.markdown("""
            <div class='cyber-card' style='text-align: center; border-color: #ff00ff;'>
                <h1 style='font-size: 8rem; margin: 0; color: #ff00ff !important;'>R</h1>
                <h2>ALEX_RIVERA</h2>
                <p>UPLINK: OAKLAND_GRID_01</p>
                <div style='background: #ff00ff; color: black; padding: 10px; font-weight: bold; margin-top: 20px;'>
                    LEVEL: 14 // ELITE_NODE
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.button("DOWNLOAD_CREDENTIAL_KEY")
        
    with c_p2:
        st.markdown("### >> NEURAL_COMPETENCIES")
        st.write("PYTHON_AUTOMATION")
        st.progress(85)
        st.write("SEO_ENGINEERING")
        st.progress(62)
        st.write("DATA_VISUALIZATION")
        st.progress(45)
        
        st.markdown("<br>### >> VERIFIED_LEDGER", unsafe_allow_html=True)
        st.markdown("""
            <div style='border: 1px solid #333; padding: 15px; margin-bottom: 10px;'>
                <p style='margin:0;'><b>TASK_ID:</b> #882 // <b>TYPE:</b> DATA_CLEAN // <b>STATUS:</b> <span style='color: #00ffff;'>COMPLETE</span></p>
            </div>
            <div style='border: 1px solid #333; padding: 15px; margin-bottom: 10px;'>
                <p style='margin:0;'><b>TASK_ID:</b> #741 // <b>TYPE:</b> SEO_AUDIT // <b>STATUS:</b> <span style='color: #00ffff;'>COMPLETE</span></p>
            </div>
            <div style='border: 1px solid #333; padding: 15px; margin-bottom: 10px;'>
                <p style='margin:0;'><b>TASK_ID:</b> #902 // <b>TYPE:</b> MARKET_RES // <b>STATUS:</b> <span style='color: #ff00ff;'>PENDING_AUTH</span></p>
            </div>
        """, unsafe_allow_html=True)
