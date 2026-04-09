from fastapi import FastAPI
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app
from env import SupplyChainEnv

app = FastAPI()

# Store multiple sessions
sessions = {}

# 🎮 Action Model (type-safe)
class Action(BaseModel):
    produce: list[int]
    ship: list[int]


# 🏠 Root endpoint (important for HF)
@app.get("/")
def home():
    return {"message": "Taycan OpenEnv is LIVE 🚀"}


# 🔄 RESET
@app.post("/reset")
def reset(difficulty: str = "easy"):
    session_id = str(uuid.uuid4())

    env = SupplyChainEnv(difficulty=difficulty)
    state = env.reset()

    sessions[session_id] = env

    return {
        "session_id": session_id,
        "state": state
    }


# 🎮 STEP
@app.post("/step/{session_id}")
def step(session_id: str, action: Action):
    env = sessions.get(session_id)

    if env is None:
        return {"error": "Invalid session_id"}

    state, reward, done, info = env.step(action.dict())

    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }


# 📊 STATE
@app.get("/state/{session_id}")
def state(session_id: str):
    env = sessions.get(session_id)

    if env is None:
        return {"error": "Invalid session_id"}

    return {
        "state": env.state()
    }
