from fastapi import FastAPI
from pydantic import BaseModel
from env import SupplyChainEnv

app = FastAPI()

# Store environment globally
env = None


@app.get("/")
def home():
    return {"message": "Taycan OpenEnv is LIVE 🚀"}


@app.post("/reset")
def reset():
    global env
    env = SupplyChainEnv(difficulty="easy")  # default

    state = env.reset()

    return {
        "state": state
    }
