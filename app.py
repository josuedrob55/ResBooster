import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vantage | Forge Your Future", page_icon="🌉", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    .stApp { background-color: #ffffff !important; }

    /* Universal Dark Text */
    html, body, [class*="st-"], .stMarkdown, p, div {
        font-family: 'Inter', sans-serif;
        color: #000000 !important;
    }

    /* Hide Streamlit default header/footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Navigation Buttons */
    .stButton > button {
        border: 2px solid #000000 !important;
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        transition: 0.3s;
        width: 100% !important;
    }
    .stButton > button:hover {
        background-color: #000000 !important;
        color: #ffffff !important;
    }

    /* HERO SECTION */
    .hero-container {
        padding: 50px 20px;
        text-align: center;
        background-color: #ffffff;
        border: 2px solid #f1f5f9;
        border-radius: 20px;
        margin-bottom: 40px;
    }

    /* CATEGORY CARDS - FIXED ALIGNMENT */
    .category-card {
        background: #ffffff;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #e2e8f0;
        text-align: left;
        min-height: 320px; /* Forces all cards to be the same height */
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }

    .category-card h1 { margin: 0 0 15px 0 !important; font-size: 40px !important; }
    .category-card h3 { color: #1e3a8a !important; font-weight: 800 !important; margin-bottom: 10px !important; }

    /* RANK BADGE - FIXED CONTRAST */
    .rank-badge {
        background-color: #1e3a8a !important; /* Deep Navy */
        color: #ffffff !important; /* Pure White Text */
        padding: 12px;
        border-radius: 12px;
        margin: 20px 0;
        font-weight: 800;
        text-align: center;
        display: block;
    }

    /* BOUNTY ITEM */
    .bounty-box {
        background: #f8fafc;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #000000;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def navigate(page_name):
    st.session_state.page = page_name

# --- TOP NAVIGATION BAR ---
col_logo, col_n1, col_n2, col_n3, col_n4 = st.columns([2, 1, 1, 1, 1])

with col_logo:
    st.markdown("<h2 style='color: #000000; margin:0; font-weight:900;'>🌉 VANTAGE</h2>", unsafe_allow_html=True)

with col_n1:
    if st.button("HOME", key="nav_h"): navigate('Home')
with col_n2:
    if st.button("BOUNTIES", key="nav_b"): navigate('Bounties')
with col_n3:
    if st.button("MISSION", key="nav_m"): navigate('About')
with col_n4:
    if st.button("PORTFOLIO", key="nav_p"): navigate('Portfolio')

st.markdown("<hr>", unsafe_allow_html=True)

# --- HOME PAGE ---
if st.session_state.page == 'Home':
    st.markdown("""
        <div class="hero-container">
            <h1 style='font-size: 3.5rem; font-weight: 900;'>Skills > Degrees.</h1>
            <p style='font-size: 1.2rem; color: #475569;'>Complete real tasks for startups. Get paid. Build a verified portfolio.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align:center; margin-bottom:30px;'>Choose Your Career Track</h2>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""<div class="category-card">
            <h1>💻</h1>
            <h3>STEM & Data</h3>
            <p>Code automation, clean data, and QA test for AI startups.</p>
        </div>""", unsafe_allow_html=True)
        st.button("VIEW TECH", key="btn_s")

    with c2:
        st.markdown("""<div class="category-card">
            <h1>📈</h1>
            <h3>Marketing</h3>
            <p>SEO audits, social strategy, and growth funnels for brands.</p>
        </div>""", unsafe_allow_html=True)
        st.button("VIEW GROWTH", key="btn_m")

    with c3:
        st.markdown("""<div class="category-card">
            <h1>📊</h1>
            <h3>Business</h3>
            <p>Market research, lead gen, and competitor analysis.</p>
        </div>""", unsafe_allow_html=True)
        st.button("VIEW BIZ", key="btn_b")

# --- MISSION PAGE ---
elif st.session_state.page == 'About':
    st.markdown("<h1 style='text-align:center;'>Our Mission</h1>", unsafe_allow_html=True)
    col_img, col_txt = st.columns([1, 1], gap="large")
    with col_img:
        st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=800")
    with col_txt:
        st.markdown("""
        <h2>Democratizing Opportunity</h2>
        <p style='font-size:1.2rem;'>Vantage was built to solve the 'Experience Gap.' We connect students from all backgrounds with micro-tasks from real companies.</p>
        <p style='font-size:1.2rem;'>Instead of an unpaid internship, we offer 'Bounties'—short, technical projects that pay cash and build your resume.</p>
        """, unsafe_allow_html=True)

# --- PORTFOLIO PAGE ---
elif st.session_state.page == 'Portfolio':
    st.markdown("<h1 style='text-align:center;'>Student Portfolio</h1>", unsafe_allow_html=True)
    p_col1, p_col2 = st.columns([1, 2], gap="large")
    with p_col1:
        st.markdown("""<div style='background:#f8fafc; padding:30px; border-radius:24px; border:2px solid #000000; text-align:center;'>
            <img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='120'>
            <h2 style='margin-top:20px;'>Alex Rivera</h2>
            <p>Oakland, CA | Student</p>
            <div class="rank-badge">
                RANK: TOP 10%
            </div>
        </div>""", unsafe_allow_html=True)
        st.button("SHARE PROFILE", key="share_btn")
    with p_col2:
        st.subheader("✅ Verified Proof of Work")
        st.markdown("""
            <div style='background:white; padding:20px; border-radius:15px; border:2px solid #e2e8f0; margin-bottom:15px;'>
                <h4 style='margin:0;'>Python Automation Script</h4>
                <p style='margin:5px 0;'>Employer: TechFlow AI • Verified 2024</p>
            </div>
        """, unsafe_allow_html=True)

# --- BOUNTIES PAGE ---
elif st.session_state.page == 'Bounties':
    st.markdown("<h1>Active Bounties</h1>", unsafe_allow_html=True)
    st.text_input("🔍 Search skills or companies...")
    st.markdown("""
        <div class="bounty-box">
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <div>
                    <h3 style='margin:0;'>Technical Lead List Generation</h3>
                    <p style='margin-top:5px;'>Track: Business Ops | Est. Time: 5 Hours</p>
                </div>
                <div style='text-align:right;'>
                    <h2 style='margin:0; color:#15803d !important;'>$120</h2>
                    <p style='margin:0;'>Reward</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("CLAIM BOUNTY BRIEF", key="claim_1")
