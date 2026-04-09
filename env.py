import numpy as np


class SupplyChainEnv:
    """
    OpenEnv-compatible Food Supply Chain Environment
    Simulates production, inventory, demand, and food expiry.
    """

    def __init__(self, difficulty="easy", seed=42):
        self.difficulty = difficulty
        self.max_steps = 30
        self.seed = seed

        np.random.seed(self.seed)

        self.reset()

    # 🔄 RESET ENVIRONMENT
    def reset(self):
        self.inventory = np.array([50, 50])   # Two products
        self.expiry = np.array([3, 5])        # Shelf life
        self.time_step = 0

        self.total_reward = 0
        self.total_waste = 0

        self.demand = self._generate_demand()

        return self.state()

    # 📊 RETURN CURRENT STATE
    def state(self):
        return {
            "inventory": self.inventory.tolist(),
            "demand": self.demand.tolist(),
            "expiry": self.expiry.tolist(),
            "costs": {
                "production": 10,
                "transport": 2,
                "storage": 1
            },
            "time_step": self.time_step
        }

    # 🎮 STEP FUNCTION
    def step(self, action):
        """
        action = {
            "produce": [int, int],
            "ship": [int, int]
        }
        """

        produce = np.array(action["produce"])
        ship = np.array(action["ship"])

        # 1. Production
        self.inventory += produce

        # 2. Fulfill demand
        sold = np.minimum(self.inventory, self.demand)
        revenue = np.sum(sold * 20)

        # 3. Update inventory
        self.inventory -= sold

        # 4. Handle expiry (waste)
        waste = self._handle_expiry()

        # 5. Costs
        production_cost = np.sum(produce * 10)
        transport_cost = np.sum(ship * 2)
        storage_cost = np.sum(self.inventory * 1)

        # 6. Demand satisfaction
        satisfaction = np.sum(sold) / (np.sum(self.demand) + 1e-6)

        # 💰 Reward Function
        reward = (
            revenue
            - production_cost
            - transport_cost
            - storage_cost
            - (waste * 15)
            + (satisfaction * 50)
        )

        # Track totals
        self.total_reward += reward
        self.total_waste += waste

        # ✅ Normalize reward (OpenEnv requirement)
        normalized_reward = max(0.0, min(1.0, reward / 1000))

        # 7. Next timestep
        self.time_step += 1
        self.demand = self._generate_demand()

        done = self.time_step >= self.max_steps

        # 🎯 Score (0 to 1)
        score = self._compute_score()

        info = {
            "waste": int(waste),
            "sold": sold.tolist(),
            "satisfaction": float(satisfaction),
            "score": float(score)
        }

        return self.state(), float(normalized_reward), done, info

    # 📉 DEMAND GENERATION (3 difficulty levels)
    def _generate_demand(self):
        if self.difficulty == "easy":
            return np.random.randint(40, 60, size=2)

        elif self.difficulty == "medium":
            return np.random.randint(20, 80, size=2)

        elif self.difficulty == "hard":
            return np.random.randint(10, 100, size=2)

        else:
            raise ValueError("Invalid difficulty level")

    # 🗑️ EXPIRY HANDLING
    def _handle_expiry(self):
        waste = 0

        for i in range(len(self.inventory)):
            if self.expiry[i] <= 1:
                waste += self.inventory[i]
                self.inventory[i] = 0

        # Reduce shelf life
        self.expiry -= 1
        self.expiry = np.maximum(self.expiry, 0)

        return waste

    # 🎯 NORMALIZED SCORE
    def _compute_score(self):
        raw_score = (self.total_reward - self.total_waste * 10) / 2000
        return max(0.0, min(1.0, raw_score))


# 🎯 TASK GRADERS (REQUIRED FOR OPENENV)

def grade_easy(env):
    return max(0.0, min(1.0, env.total_reward / 2000))


def grade_medium(env):
    score = env.total_reward - env.total_waste * 2
    return max(0.0, min(1.0, score / 2000))


def grade_hard(env):
    score = env.total_reward - env.total_waste * 5
    return max(0.0, min(1.0, score / 2000))


# 🧪 TEST RUN
if __name__ == "__main__":
    env = SupplyChainEnv(difficulty="medium")

    state = env.reset()
    print("Initial State:", state)

    done = False

    while not done:
        action = {
            "produce": state["demand"],
            "ship": state["demand"]
        }

        state, reward, done, info = env.step(action)

        print("\nStep:", state["time_step"])
        print("State:", state)
        print("Reward:", reward)
        print("Info:", info)

    print("\n✅ FINAL SCORE:", info["score"])
