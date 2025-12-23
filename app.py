import streamlit as st
import uuid
from datetime import datetime

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="VANTAGE // PROTOCOL",
    page_icon="🧬",
    layout="wide"
)

st.title("VANTAGE // PROTOCOL")

# -----------------------------
# IN-MEMORY DATABASE
# -----------------------------
if "users" not in st.session_state:
    st.session_state.users = {
        "alex": {"role": "student"},
        "genisys": {"role": "company"}
    }

if "bounties" not in st.session_state:
    st.session_state.bounties = []

if "submissions" not in st.session_state:
    st.session_state.submissions = []

if "current_user" not in st.session_state:
    st.session_state.current_user = None

# -----------------------------
# LOGIN GATE (VISIBLE)
# -----------------------------
if not st.session_state.current_user:
    st.subheader("CONNECT TO VANTAGE")

    user = st.selectbox("SELECT IDENTITY", list(st.session_state.users.keys()))
    if st.button("CONNECT"):
        st.session_state.current_user = user
        st.rerun()

    st.stop()

# -----------------------------
# SESSION INFO
# -----------------------------
user = st.session_state.current_user
role = st.session_state.users[user]["role"]

st.sidebar.markdown(f"**USER:** `{user.upper()}`")
st.sidebar.markdown(f"**ROLE:** `{role.upper()}`")

if st.sidebar.button("DISCONNECT"):
    st.session_state.current_user = None
    st.rerun()

# -----------------------------
# NAV
# -----------------------------
page = st.sidebar.radio(
    "NAVIGATION",
    ["Dashboard", "Bounties", "Submit Work", "Verify Work", "Neural Identity"]
)

# -----------------------------
# DASHBOARD
# -----------------------------
if page == "Dashboard":
    st.header("COMMAND_CENTER")
    st.metric("ACTIVE BOUNTIES", len(st.session_state.bounties))
    st.metric(
        "VERIFIED PROOFS",
        len([s for s in st.session_state.submissions if s["status"] == "VERIFIED"])
    )

# -----------------------------
# BOUNTIES
# -----------------------------
elif page == "Bounties":
    st.header("BOUNTY_TERMINAL")

    if role == "company":
        st.subheader("POST NEW BOUNTY")
        with st.form("post_bounty"):
            title = st.text_input("TASK NAME")
            reward = st.number_input("REWARD (CR)", min_value=50)
            hours = st.selectbox("TIME ESTIMATE", ["4–6h", "6–8h", "8–10h"])
            skills = st.text_input("SKILLS (comma separated)")
            if st.form_submit_button("DEPLOY"):
                st.session_state.bounties.append({
                    "id": str(uuid.uuid4())[:8],
                    "title": title,
                    "reward": reward,
                    "hours": hours,
                    "skills": skills,
                    "company": user,
                    "claimed_by": None
                })
                st.success("BOUNTY DEPLOYED")

    st.subheader("AVAILABLE BOUNTIES")
    for b in st.session_state.bounties:
        st.markdown(f"""
**{b['title']}**  
ID: `{b['id']}`  
REWARD: {b['reward']} CR | TIME: {b['hours']}  
SKILLS: {b['skills']}  
COMPANY: {b['company']}
""")
        if role == "student" and not b["claimed_by"]:
            if st.button(f"CLAIM {b['id']}", key=f"claim_{b['id']}"):
                b["claimed_by"] = user
                st.success("BOUNTY CLAIMED")

# -----------------------------
# SUBMIT WORK
# -----------------------------
elif page == "Submit Work":
    if role != "student":
        st.warning("STUDENT ACCESS ONLY")
        st.stop()

    st.header("SUBMIT_DELIVERABLE")

    claimed = [b for b in st.session_state.bounties if b["claimed_by"] == user]

    if not claimed:
        st.info("NO CLAIMED BOUNTIES")
        st.stop()

    bounty = st.selectbox("SELECT BOUNTY", claimed, format_func=lambda x: x["title"])

    with st.form("submit_work"):
        link = st.text_input("DELIVERABLE LINK (GitHub / Drive)")
        process = st.text_area("PROCESS LOG (REQUIRED — describe steps)")
        if st.form_submit_button("TRANSMIT"):
            if len(process) < 50:
                st.error("PROCESS LOG TOO SHORT (MIN 50 CHARS)")
            else:
                st.session_state.submissions.append({
                    "id": bounty["id"],
                    "student": user,
                    "company": bounty["company"],
                    "link": link,
                    "process": process,
                    "status": "PENDING",
                    "timestamp": datetime.utcnow()
                })
                st.success("SUBMISSION SENT FOR VERIFICATION")

# -----------------------------
# VERIFY WORK
# -----------------------------
elif page == "Verify Work":
    if role != "company":
        st.warning("COMPANY ACCESS ONLY")
        st.stop()

    st.header("VALIDATION_QUEUE")

    queue = [s for s in st.session_state.submissions if s["company"] == user]

    if not queue:
        st.info("NO SUBMISSIONS")
        st.stop()

    for s in queue:
        st.markdown(f"""
**TASK ID:** `{s['id']}`  
STUDENT: {s['student']}  
LINK: {s['link']}  
STATUS: {s['status']}
""")
        with st.expander("PROCESS LOG"):
            st.write(s["process"])

        if s["status"] == "PENDING":
            col1, col2 = st.columns(2)
            if col1.button(f"VERIFY {s['id']}", key=f"v_{s['id']}"):
                s["status"] = "VERIFIED"
                st.success("VERIFIED")
            if col2.button(f"REJECT {s['id']}", key=f"r_{s['id']}"):
                s["status"] = "REJECTED"
                st.error("REJECTED")

# -----------------------------
# NEURAL IDENTITY
# -----------------------------
elif page == "Neural Identity":
    st.header("NEURAL_IDENTITY")

    ledger = [
        s for s in st.session_state.submissions
        if s["student"] == user and s["status"] == "VERIFIED"
    ]

    if not ledger:
        st.info("NO VERIFIED PROOFS YET")
    else:
        for l in ledger:
            st.markdown(f"""
✅ **{l['id']}**  
COMPANY: {l['company']}  
TIMESTAMP: {l['timestamp']}
""")
