from fastapi import FastAPI
from pydantic import BaseModel
from env import SupplyChainEnv

app = FastAPI()

# Global environment instance
env = None


# ✅ Root check
@app.get("/")
def home():
    return {"message": "Taycan OpenEnv is LIVE 🚀"}


# ✅ Action schema
class Action(BaseModel):
    produce: list[int]
    ship: list[int]


# 🔄 RESET ENDPOINT
@app.post("/reset")
def reset():
    global env
    env = SupplyChainEnv(difficulty="easy")  # default task

    state = env.reset()

    return {
        "state": state
    }


# 🎮 STEP ENDPOINT
@app.post("/step")
def step(action: Action):
    global env

    if env is None:
        return {"error": "Environment not initialized. Call /reset first."}

    state, reward, done, info = env.step(action.dict())

    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }


# 📊 STATE ENDPOINT
@app.get("/state")
def state():
    global env

    if env is None:
        return {"error": "Environment not initialized. Call /reset first."}

    return {
        "state": env.state()
    }
