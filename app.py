import streamlit as st
import uuid
from datetime import datetime

# =====================================================
# CONFIG
# =====================================================
st.set_page_config(
    page_title="VANTAGE // NEURAL PROTOCOL",
    page_icon="🧬",
    layout="wide"
)

# =====================================================
# CYBER UI ENGINE (SAFE)
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300;500&display=swap');

html, body, .stApp {
    background-color: #05050A;
    color: #CBD5E1;
    font-family: 'JetBrains Mono', monospace;
}

/* Subtle grid */
.stApp {
    background-image:
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 60px 60px;
}

/* Headings */
h1, h2, h3 {
    font-family: 'Orbitron', sans-serif;
    letter-spacing: 3px;
    color: #00F0FF;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: rgba(10,10,15,0.95);
    border-right: 1px solid #111827;
    backdrop-filter: blur(16px);
}

/* Cards */
.v-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 22px;
    border-radius: 14px;
    transition: 0.3s;
    margin-bottom: 18px;
}
.v-card:hover {
    border-color: #00F0FF;
    box-shadow: 0 0 25px rgba(0,240,255,0.25);
    transform: translateY(-2px);
}

/* Tags */
.tag {
    font-size: 11px;
    padding: 4px 8px;
    border-radius: 6px;
    margin-right: 6px;
}
.stem { background: rgba(0,240,255,0.15); color: #00F0FF; }
.growth { background: rgba(255,0,200,0.15); color: #FF4FD8; }
.intel { background: rgba(255,176,32,0.15); color: #FFB020; }

/* Status */
.verified { color: #22C55E; }
.pending { color: #FACC15; }
.rejected { color: #EF4444; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>VANTAGE // NEURAL PROTOCOL</h1>", unsafe_allow_html=True)

# =====================================================
# STATE
# =====================================================
if "users" not in st.session_state:
    st.session_state.users = {
        "alex": {"role": "student", "xp": 120},
        "genisys": {"role": "company", "xp": 0}
    }

if "bounties" not in st.session_state:
    st.session_state.bounties = []

if "submissions" not in st.session_state:
    st.session_state.submissions = []

if "current_user" not in st.session_state:
    st.session_state.current_user = None

# =====================================================
# LOGIN
# =====================================================
if not st.session_state.current_user:
    st.subheader("INITIALIZE NEURAL LINK")
    user = st.selectbox("IDENTITY", list(st.session_state.users.keys()))
    if st.button("CONNECT"):
        st.session_state.current_user = user
        st.rerun()
    st.stop()

user = st.session_state.current_user
role = st.session_state.users[user]["role"]

# =====================================================
# SIDEBAR HUD
# =====================================================
st.sidebar.markdown(f"### {user.upper()}")
st.sidebar.markdown(f"ROLE: `{role.upper()}`")
st.sidebar.markdown(f"XP: `{st.session_state.users[user]['xp']}`")
st.sidebar.progress(min(st.session_state.users[user]['xp'] / 500, 1.0))

if st.sidebar.button("DISCONNECT"):
    st.session_state.current_user = None
    st.rerun()

page = st.sidebar.radio(
    "NAV",
    ["Command Center", "Bounty Terminal", "Submit Work", "Validation Queue", "Neural Identity"]
)

# =====================================================
# COMMAND CENTER
# =====================================================
if page == "Command Center":
    st.subheader("SYSTEM STATUS")

    c1, c2, c3 = st.columns(3)
    c1.metric("ACTIVE BOUNTIES", len(st.session_state.bounties))
    c2.metric("VERIFIED WORK", len([s for s in st.session_state.submissions if s["status"] == "VERIFIED"]))
    c3.metric("NETWORK LATENCY", "14ms")

# =====================================================
# BOUNTY TERMINAL
# =====================================================
elif page == "Bounty Terminal":
    st.subheader("AVAILABLE MICRO-BOUNTIES")

    if role == "company":
        with st.form("deploy"):
            st.markdown("### DEPLOY BOUNTY")
            title = st.text_input("TASK")
            domain = st.selectbox("DOMAIN", ["STEM", "GROWTH", "INTEL"])
            reward = st.number_input("REWARD (CR)", min_value=50)
            if st.form_submit_button("DEPLOY"):
                st.session_state.bounties.append({
                    "id": str(uuid.uuid4())[:8],
                    "title": title,
                    "domain": domain,
                    "reward": reward,
                    "company": user,
                    "claimed_by": None
                })

    for b in st.session_state.bounties:
        domain_class = b["domain"].lower()
        st.markdown(f"""
        <div class="v-card">
            <h3>{b['title']}</h3>
            <span class="tag {domain_class}">{b['domain']}</span>
            <p>REWARD: {b['reward']} CR</p>
            <p>COMPANY: {b['company']}</p>
        </div>
        """, unsafe_allow_html=True)

        if role == "student" and not b["claimed_by"]:
            if st.button(f"CLAIM {b['id']}"):
                b["claimed_by"] = user
                st.session_state.users[user]["xp"] += 10

# =====================================================
# SUBMIT WORK
# =====================================================
elif page == "Submit Work":
    if role != "student":
        st.warning("STUDENT ACCESS ONLY")
        st.stop()

    claimed = [b for b in st.session_state.bounties if b["claimed_by"] == user]
    if not claimed:
        st.info("NO ACTIVE BOUNTIES")
        st.stop()

    bounty = st.selectbox("SELECT TASK", claimed, format_func=lambda x: x["title"])

    with st.form("submit"):
        link = st.text_input("DELIVERABLE LINK")
        process = st.text_area("PROCESS LOG")
        if st.form_submit_button("TRANSMIT"):
            if len(process) < 50:
                st.error("PROCESS LOG TOO SHORT")
            else:
                st.session_state.submissions.append({
                    "id": bounty["id"],
                    "student": user,
                    "company": bounty["company"],
                    "status": "PENDING"
                })
                st.session_state.users[user]["xp"] += 50

# =====================================================
# VALIDATION
# =====================================================
elif page == "Validation Queue":
    if role != "company":
        st.warning("COMPANY ACCESS ONLY")
        st.stop()

    for s in st.session_state.submissions:
        if s["company"] == user:
            status_class = s["status"].lower()
            st.markdown(f"""
            <div class="v-card">
                <p>TASK: {s['id']}</p>
                <p>STUDENT: {s['student']}</p>
                <p class="{status_class}">STATUS: {s['status']}</p>
            </div>
            """, unsafe_allow_html=True)

            if s["status"] == "PENDING":
                if st.button(f"VERIFY {s['id']}"):
                    s["status"] = "VERIFIED"
                    st.session_state.users[s["student"]]["xp"] += 100

# =====================================================
# NEURAL IDENTITY
# =====================================================
elif page == "Neural Identity":
    st.subheader("VERIFIED PROOF-OF-WORK LEDGER")

    for s in st.session_state.submissions:
        if s["student"] == user and s["status"] == "VERIFIED":
            st.markdown(f"""
            <div class="v-card verified">
                ✔ TASK {s['id']} — VERIFIED
            </div>
            """, unsafe_allow_html=True)
