import requests

BASE_URL = "https://taycan-food-supply-chain.hf.space"

print("[START]")

res = requests.post(f"{BASE_URL}/reset", json={})
state = res.json()

for i in range(5):
    action = {"produce": [20, 20], "ship": [15, 15]}
    res = requests.post(f"{BASE_URL}/step", json=action)
    data = res.json()

    print(f"[STEP] {i} reward={data['reward']} score={data['info']['score']}")

print("[END]")
