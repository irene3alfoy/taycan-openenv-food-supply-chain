from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from env import SupplyChainEnv

app = FastAPI(title="Taycan OpenEnv Food Supply Chain")

# -----------------------------
# Models (Typed API)
# -----------------------------
class Action(BaseModel):
    produce: List[int]
    ship: List[int]


class StepResponse(BaseModel):
    state: dict
    reward: float
    done: bool
    info: dict


# -----------------------------
# Environment Instance
# -----------------------------
env = SupplyChainEnv(difficulty="medium")


# -----------------------------
# Routes
# -----------------------------
@app.get("/")
def home():
    return {"message": "Taycan OpenEnv is running 🚀"}


@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}


@app.get("/state")
def get_state():
    return {"state": env.state()}


@app.post("/step", response_model=StepResponse)
def step(action: Action):
    state, reward, done, info = env.step(action.dict())

    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }
