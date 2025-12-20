import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vantage | Forge Your Future", page_icon="🌉", layout="wide")

# --- MODERN CSS UI ---
st.markdown("""
    <style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main Background & Fonts */
    .stApp {
        background-color: #ffffff;
        font-family: 'Inter', -apple-system, sans-serif;
    }
    
    /* Hero Section */
    .hero-container {
        padding: 60px 20px;
        text-align: center;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 40px;
    }
    
    /* Custom Cards */
    .card {
        background-color: #f9fafb;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        cursor: pointer;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        border-color: #3b82f6;
    }
    
    /* Buttons */
    .stButton>button {
        border-radius: 10px;
        background-color: #1e3a8a;
        color: white;
        font-weight: 600;
        border: none;
        padding: 10px 24px;
    }
    
    /* Navigation Bar Replacement */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px;
        margin-bottom: 30px;
        border-bottom: 1px solid #f3f4f6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE FOR NAVIGATION ---
# This allows us to switch pages without using the sidebar
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def set_page(page_name):
    st.session_state.page = page_name

# --- CUSTOM TOP NAV ---
col_nav1, col_nav2 = st.columns([1, 1])
with col_nav1:
    st.markdown("### 🌉 VANTAGE")
with col_nav2:
    cols = st.columns(4)
    if cols[0].button("Home"): set_page('Home')
    if cols[1].button("Bounties"): set_page('Bounties')
    if cols[2].button("About"): set_page('About')
    if cols[3].button("Portfolio"): set_page('Portfolio')

st.divider()

# --- HOME PAGE ---
if st.session_state.page == 'Home':
    st.markdown("""
        <div class="hero-container">
            <h1 style='font-size: 3.5rem; margin-bottom: 10px;'>Experience is the new Resume.</h1>
            <p style='font-size: 1.2rem; opacity: 0.9;'>Complete technical projects for real companies. Get paid. Get verified.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("### 🚀 Start Building")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class="card"><h3>💻 STEM</h3><p>Code scripts, clean data, or run QA tests for startups.</p></div>""", unsafe_allow_html=True)
        if st.button("Explore Tech", key="btn_stem"): set_page('Bounties')
        
    with col2:
        st.markdown("""<div class="card"><h3>📈 Marketing</h3><p>Design SEO audits, social kits, and growth strategies.</p></div>""", unsafe_allow_html=True)
        if st.button("Explore Creative", key="btn_mkt"): set_page('Bounties')
        
    with col3:
        st.markdown("""<div class="card"><h3>📊 Business</h3><p>Competitive research, lead generation, and pitch decks.</p></div>""", unsafe_allow_html=True)
        if st.button("Explore Biz", key="btn_biz"): set_page('Bounties')

# --- BOUNTIES PAGE ---
elif st.session_state.page == 'Bounties':
    st.header("🎯 Active Bounties")
    st.write("Pick a project and start forging your career.")
    
    tab1, tab2, tab3 = st.tabs(["All Bounties", "Drafts", "Completed"])
    
    with tab1:
        # Example Bounty 1
        with st.container():
            c1, c2, c3 = st.columns([0.5, 3, 1])
            c1.markdown("## 🍪") # Icon for company
            with c2:
                st.markdown("#### Competitor SEO Keyword Map")
                st.caption("Company: SmartBites | Major: Marketing/English")
            with c3:
                st.markdown("### $120")
                if st.button("View Brief", key="b1"): st.info("Briefing details would expand here...")
            st.divider()

# --- ABOUT PAGE ---
elif st.session_state.page == 'About':
    st.header("About Vantage")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("""
        ### Our Mission
        We believe that where you come from shouldn't dictate where you go. 
        Vantage was built to bridge the "Experience Gap" for students—especially 
        those in underrepresented communities who don't have a network in tech.
        
        ### How it works
        1. **Companies** post specific, technical tasks they need done.
        2. **Students** complete the tasks as part of a competition.
        3. **Winners** get paid; **Everyone** gets a verified proof-of-work entry for their resume.
        """)
    with col_b:
        st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&q=80&w=1000", use_column_width=True)

# --- PORTFOLIO PAGE ---
elif st.session_state.page == 'Portfolio':
    st.header("👤 Student Portfolio")
    st.write("This is your public-facing 'Proof of Work' page.")
    
    col_p1, col_p2 = st.columns([1, 2])
    with col_p1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)
        st.subheader("Alex Rivera")
        st.caption("East Bay, California")
        st.write("🏆 **Vantage Rank:** Top 10%")
    
    with col_p2:
        st.markdown("#### ✅ Verified Projects")
        st.info("**Lead Gen Spreadsheet** - *TechStream AI* (Verified Oct 2024)")
        st.info("**SEO Keyword Audit** - *Main St. Bakery* (Verified Sept 2024)")
        st.button("Export Verified Resume")
