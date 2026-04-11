from fastapi import FastAPI

app = FastAPI()

current_state = {
    "inventory": [50, 50],
    "demand": [20, 20]
}

@app.get("/")
def home():
    return {"message": "Taycan OpenEnv is LIVE 🚀"}

@app.post("/reset")
def reset(data: dict = {}):
    return {"state": {"inventory": [50,50]}
    }
    return {"state": current_state}

@app.post("/step")
def step(action: dict):
    global current_state

    produce = action.get("produce", [0, 0])
    ship = action.get("ship", [0, 0])

    current_state["inventory"] = [
        current_state["inventory"][0] + produce[0] - ship[0],
        current_state["inventory"][1] + produce[1] - ship[1]
    ]

    reward = sum(ship) - sum(produce) * 0.5
    score = max(0, min(1, reward / 50))

    return {
        "state": current_state,
        "reward": reward,
        "done": False,
        "info": {"score": score}
    }

@app.get("/state")
def state():
    return current_state
