import streamlit as st
import pandas as pd

# Setting up the App Page
st.set_page_config(page_title="BridgeBounty MVP", layout="wide")

# Sidebar for Navigation
st.sidebar.title("🌉 BridgeBounty")
st.sidebar.info("The Work-Experience Marketplace for High School & College Students")
menu = st.sidebar.radio("Navigation", ["Project Feed", "My Portfolio", "Submit a Project", "Employer Dashboard"])

# Mock Data for Projects
projects = [
    {"id": 1, "title": "Social Media Content Kit", "company": "Eco-Coffee Co.", "category": "Marketing", "bounty": "$75", "difficulty": "Entry", "type": "Deliverable"},
    {"id": 2, "title": "Competitor Pricing Analysis", "company": "TechStart AI", "category": "Business", "bounty": "$120", "difficulty": "Intermediate", "type": "Technical"},
    {"id": 3, "title": "Python Data Cleaning Script", "company": "DataFlow", "category": "STEM", "bounty": "$200", "difficulty": "Advanced", "type": "Code"},
    {"id": 4, "title": "Local Event Flyer Set", "company": "City Parks Dept", "category": "Design", "bounty": "$50", "difficulty": "Entry", "type": "Asset Creation"},
]

# --- PROJECT FEED ---
if menu == "Project Feed":
    st.header("🎯 Open Bounties")
    st.write("Complete a task, get paid, and get a 'Verified' badge for your resume.")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("Filter by Major/Skill", ["All", "Marketing", "Business", "STEM", "Design"])
    with col2:
        region = st.selectbox("Filter by Region", ["All", "Underrepresented Communities", "National", "Remote"])

    st.divider()

    for p in projects:
        if category == "All" or p["category"] == category:
            with st.container():
                c1, c2, c3 = st.columns([3, 1, 1])
                with c1:
                    st.subheader(p["title"])
                    st.caption(f"Posted by: {p['company']} | Type: {p['type']}")
                with c2:
                    st.write(f"**Bounty:** {p['bounty']}")
                    st.write(f"Level: {p['difficulty']}")
                with c3:
                    if st.button(f"View Brief", key=p["id"]):
                        st.session_state.current_project = p
                st.divider()

# --- SUBMISSION LOGIC (The "Anti-Plagiarism" Template) ---
if menu == "Submit a Project":
    st.header("📤 Submit Your Deliverable")
    st.write("Follow the template below to ensure your work is 'Verified Ready'.")
    
    project_title = st.selectbox("Which project are you submitting?", [p["title"] for p in projects])
    
    st.info("💡 BridgeBounty Tip: Employers value your *process* as much as your final result.")
    
    with st.form("submission_form"):
        st.text_input("Link to Final Work (Google Drive, GitHub, Figma, etc.)")
        st.text_area("Process Log: Explain the 3 steps you took to complete this.")
        st.text_area("Research Sources: What sites/tools did you use?")
        st.checkbox("I certify this is my original work and not generated solely by AI.")
        submitted = st.form_submit_button("Submit for Review")
        if submitted:
            st.success("Project submitted! The employer has 72 hours to review.")

# --- MY PORTFOLIO (The Resume Builder) ---
if menu == "My Portfolio":
    st.header("👤 Your Verified Proof-of-Work")
    st.write("Share this link with College Admissions or Job Recruiters.")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/150", caption="Student Profile")
        st.write("**Name:** Alex Smith")
        st.write("**Location:** East Oakland, CA")
        st.write("**Badges:** 🏆 Top 10% Marketer | ✅ 5 Projects Completed")
    
    with col2:
        st.subheader("Verified Project History")
        st.success("✅ **Social Media Content Kit** for *Eco-Coffee Co.* (March 2024)")
        st.info("✅ **Competitive Analysis Spreadsheet** for *TechStart AI* (Feb 2024)")
        st.write("---")
        st.write("🔗 [Download BridgeBounty Verified Resume PDF]")

# --- EMPLOYER DASHBOARD ---
if menu == "Employer Dashboard":
    st.header("🏢 Employer Control Center")
    st.write("Review submissions from talented students.")
    
    st.metric("Total Submissions", "24", "+12% this week")
    
    st.subheader("Submissions for 'Social Media Content Kit'")
    st.write("1. **Student A** (Title I School) - [View Submission]")
    st.write("2. **Student B** (Bay Area) - [View Submission]")
    st.button("Pick Winner & Release Bounty")