import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vantage | Forge Your Future", page_icon="🌉", layout="wide")

# --- HIGH-END SaaS CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* Global Reset */
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
        color: #1e293b; /* Deep Slate for all text */
    }

    /* Remove Streamlit default padding and bars */
    .block-container { padding-top: 2rem; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* HERO SECTION: Dark Navy with Crisp White/Silver Text */
    .hero-section {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        padding: 80px 40px;
        border-radius: 30px;
        text-align: center;
        margin-bottom: 50px;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    }
    
    .hero-section h1 {
        color: #ffffff !important;
        font-size: 4rem !important;
        font-weight: 800 !important;
        margin-bottom: 20px !important;
        line-height: 1.1;
    }
    
    .hero-section p {
        color: #cbd5e1 !important; /* Silver-grey for readability */
        font-size: 1.4rem !important;
        max-width: 850px;
        margin: 0 auto !important;
        line-height: 1.6;
    }

    /* CARD DESIGN: Deep Contrast */
    .category-card {
        background: #ffffff;
        padding: 40px;
        border-radius: 24px;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .category-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.1);
        border-color: #3b82f6;
    }

    .category-card h3 {
        color: #0f172a !important; /* Force black-ish text */
        font-weight: 700 !important;
        margin-bottom: 15px !important;
    }

    .category-card p {
        color: #475569 !important; /* Strong grey text */
        line-height: 1.6;
    }

    /* BOUNTY CARDS */
    .bounty-item {
        background: white;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    /* BUTTONS: Deep Navy */
    .stButton > button {
        border-radius: 12px !important;
        background-color: #1e3a8a !important;
        color: white !important;
        border: none !important;
        font-weight: 600 !important;
        transition: 0.2s;
    }
    
    .stButton > button:hover {
        background-color: #2563eb !important;
        transform: scale(1.02);
    }

    /* Text Overrides to prevent White-on-White */
    h1, h2, h3, h4, p, span, li {
        color: #0f172a !important;
    }
    .hero-section * {
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def navigate_to(page_name):
    st.session_state.page = page_name

# --- TOP NAVIGATION BAR ---
col_logo, col_nav = st.columns([1, 2])
with col_logo:
    st.markdown("<h2 style='color: #1e3a8a; margin:0; font-weight:800;'>🌉 VANTAGE</h2>", unsafe_allow_html=True)

with col_nav:
    n1, n2, n3, n4 = st.columns(4)
    if n1.button("Home"): navigate_to('Home')
    if n2.button("Explore"): navigate_to('Bounties')
    if n3.button("Mission"): navigate_to('About')
    if n4.button("Portfolio"): navigate_to('Portfolio')

st.markdown("<br>", unsafe_allow_html=True)

# --- HOME PAGE ---
if st.session_state.page == 'Home':
    st.markdown("""
        <div class="hero-section">
            <h1>Proof of skill is the <br>new pedigree.</h1>
            <p>Skip the networking. Complete technical bounties for top companies <br>and build a verified portfolio that opens doors.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align:center; margin-bottom:40px;'>Select Your Career Track</h2>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""<div class="category-card">
            <h1 style='font-size:30px; margin-bottom:10px;'>💻</h1>
            <h3>STEM & Data</h3>
            <p>Build automation scripts, perform QA testing, or clean data for scaling AI startups.</p>
        </div>""", unsafe_allow_html=True)
        st.button("Explore Tech", key="go_stem", use_container_width=True)

    with c2:
        st.markdown("""<div class="category-card">
            <h1 style='font-size:30px; margin-bottom:10px;'>📈</h1>
            <h3>Growth & Marketing</h3>
            <p>Execute SEO audits, design social kits, and build growth funnels for real brands.</p>
        </div>""", unsafe_allow_html=True)
        st.button("Explore Marketing", key="go_mkt", use_container_width=True)

    with c3:
        st.markdown("""<div class="category-card">
            <h3>📊 Business Ops</h3>
            <p>Conduct competitor research, build lead lists, and create high-stakes pitch decks.</p>
        </div>""", unsafe_allow_html=True)
        st.button("Explore Business", key="go_biz", use_container_width=True)

# --- MISSION PAGE ---
elif st.session_state.page == 'About':
    st.markdown("<h1 style='text-align:center;'>Our Mission</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_img, col_txt = st.columns([1, 1.2], gap="large")
    with col_img:
        st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=800")
    
    with col_txt:
        st.markdown("""
        <h2 style='margin-top:0;'>Bridging the Talent Gap</h2>
        <p style='font-size:1.1rem; color:#475569;'>Traditional internships favor those with existing networks. We’re changing the rules.</p>
        <p style='font-size:1.1rem; color:#475569;'>Vantage is a <b>Work-Experience Marketplace</b>. We allow companies to outsource small technical tasks to high school and college students.</p>
        <hr>
        <h4>The Outcome?</h4>
        <p style='color:#475569;'>Students get paid and earn a 'Verified Proof of Work'—a digital credential that proves to any recruiter or admissions officer exactly what they are capable of.</p>
        """, unsafe_allow_html=True)

# --- PORTFOLIO PAGE ---
elif st.session_state.page == 'Portfolio':
    st.markdown("<h1 style='text-align:center;'>Your Digital Credential</h1>", unsafe_allow_html=True)
    
    p_col1, p_col2 = st.columns([1, 2], gap="large")
    with p_col1:
        st.markdown("""<div style='background:#ffffff; padding:40px; border-radius:30px; border:1px solid #e2e8f0; text-align:center;'>
            <img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='140'>
            <h2 style='margin-top:20px; color:#0f172a;'>Alex Rivera</h2>
            <p style='color:#64748b;'>Oakland, CA | Student</p>
            <div style='background:#f1f5f9; padding:10px; border-radius:10px; margin:20px 0;'>
                <p style='margin:0; font-weight:700; color:#1e3a8a;'>Top 10% Platform Rank</p>
            </div>
            <button style='width:100%; padding:10px; border-radius:10px; border:1px solid #1e3a8a; background:none; color:#1e3a8a; font-weight:600;'>Share Profile</button>
        </div>""", unsafe_allow_html=True)
        
    with p_col2:
        st.subheader("✅ Verified Proof of Work")
        st.markdown("""
            <div style='background:white; padding:20px; border-radius:15px; border:1px solid #e2e8f0; margin-bottom:15px;'>
                <h4 style='margin:0;'>Python Data Cleaning Script</h4>
                <p style='color:#64748b; margin:5px 0;'>Employer: TechFlow AI • Verified Oct 2024</p>
            </div>
            <div style='background:white; padding:20px; border-radius:15px; border:1px solid #e2e8f0; margin-bottom:15px;'>
                <h4 style='margin:0;'>SEO Competitor Audit</h4>
                <p style='color:#64748b; margin:5px 0;'>Employer: SmartBites Bakery • Verified Sept 2024</p>
            </div>
        """, unsafe_allow_html=True)

# --- BOUNTIES PAGE ---
elif st.session_state.page == 'Bounties':
    st.markdown("<h1 style='text-align:center;'>Available Bounties</h1>", unsafe_allow_html=True)
    
    st.text_input("🔍 Search skills, companies, or tracks...")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Bounty Card 1
    st.markdown("""
        <div style='background: white; padding:30px; border-radius:20px; border:1px solid #e2e8f0; border-left: 8px solid #1e3a8a; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);'>
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <div>
                    <h3 style='margin:0; color:#0f172a;'>Product Market Research Deck</h3>
                    <p style='color:#64748b; margin-top:5px;'>Track: Business Ops | Est. Time: 6 Hours</p>
                </div>
                <div style='text-align:right;'>
                    <h2 style='margin:0; color:#166534;'>$150</h2>
                    <p style='color:#64748b; margin:0;'>Reward</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("Claim Bounty Brief", key="b1")
