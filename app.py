from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

app = FastAPI()

# In-memory DB for MVP
users = {
    "alex": {"role": "student", "xp": 120, "level": 2},
    "genisys": {"role": "company", "xp": 0, "level": 0}
}
bounties = []
submissions = []

# Models
class Bounty(BaseModel):
    id: str
    title: str
    reward: int
    skills: str
    company: str
    claimed_by: Optional[str] = None
    hours: str

class Submission(BaseModel):
    id: str
    bounty_id: str
    student: str
    company: str
    link: str
    process: str
    status: str
    timestamp: datetime

# Routes
@app.get("/bounties")
def get_bounties():
    return bounties

@app.post("/bounties")
def add_bounty(b: Bounty):
    bounties.append(b.dict())
    return {"message": "Bounty added"}

@app.get("/submissions")
def get_submissions():
    return submissions

@app.post("/submissions")
def add_submission(s: Submission):
    submissions.append(s.dict())
    return {"message": "Submission added"}

@app.post("/verify/{submission_id}")
def verify_submission(submission_id: str):
    for s in submissions:
        if s["id"] == submission_id:
            s["status"] = "VERIFIED"
            users[s["student"]]["xp"] += s["reward"]
            users[s["student"]]["level"] = users[s["student"]]["xp"] // 100 + 1
            return {"message": "Verified"}
    return {"error": "Not found"}
