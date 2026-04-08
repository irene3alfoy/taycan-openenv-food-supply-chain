import requests
import os
import time

BASE_URL = os.getenv("API_BASE_URL", "https://taycan-food-supply-chain.hf.space")

print("[START] Running inference")

def run_task(difficulty):
    print(f"[STEP] Starting task: {difficulty}")

    # reset
    res = requests.post(f"{BASE_URL}/reset", json={"difficulty": difficulty})
    state = res.json()

    total_score = 0

    for step in range(10):
        action = {
            "produce": state.get("demand", [20, 20]),
            "ship": state.get("demand", [20, 20])
        }

        res = requests.post(f"{BASE_URL}/step", json=action)
        data = res.json()

        state = data["state"]
        reward = data["reward"]
        score = data["info"]["score"]

        total_score += score

        print(f"[STEP] step={step} reward={reward} score={score}")

        if data["done"]:
            break

    avg_score = total_score / (step + 1)

    print(f"[STEP] Completed task {difficulty} avg_score={avg_score}")

    return avg_score


results = {}

for level in ["easy", "medium", "hard"]:
    score = run_task(level)
    results[level] = score

print("[END] Final Results:", results)
