# 🚀 Taycan: OpenEnv Food Supply Chain Optimization Environment

## 🌍 Overview
Taycan OpenEnv is a real-world AI simulation of a food supply chain where agents optimize **production, shipping, inventory, and waste reduction**.

It models real operational challenges such as:
- Demand uncertainty
- Inventory mismanagement
- Food spoilage
- Cost optimization

Built using **OpenEnv standards**, Taycan enables reinforcement learning agents to interact through:
- `reset()`
- `step()`
- `state()`

Deployed using **FastAPI + Docker on Hugging Face Spaces**, making it scalable and reproducible.

---

## ❗ Problem Statement

Modern food supply chains suffer from:
- High food wastage due to spoilage
- Unpredictable demand patterns
- Inefficient inventory management
- Lack of AI-ready simulation environments

There is no standardized environment where AI agents can learn to optimize such real-world systems.

---

## 💡 Solution

Taycan provides:
- A **realistic supply chain simulation**
- A **reinforcement learning-compatible environment**
- A **standardized OpenEnv API**
- A **scalable backend for experimentation**

---

## ⚙️ Features

### 🧠 Dynamic Environment
- Inventory tracking
- Demand generation (stochastic)
- Product expiry & spoilage
- Cost modeling (production, transport, storage)

### 🎯 Difficulty Levels
| Level   | Description |
|--------|------------|
| Easy   | Stable demand |
| Medium | Moderate fluctuations |
| Hard   | High uncertainty + spoilage |

---

## 🔌 API Endpoints

- `POST /reset` → Initialize environment  
- `POST /step/{session_id}` → Apply action  
- `GET /state/{session_id}` → Get current state  

---

## 🎯 Tasks & Evaluation

### 🟢 Easy Task
- Stable demand
- Low waste
- Objective: Maintain steady profit

### 🟡 Medium Task
- Demand fluctuations
- Objective: Balance supply and demand

### 🔴 Hard Task
- High uncertainty
- High spoilage penalties
- Objective: Optimize under risk


🌟 What Makes Taycan Unique
Real-world supply chain simulation (not a toy problem)
Multi-objective reward system
OpenEnv-compliant API
Deployable and scalable via Hugging Face

👥 Team Taycan
Deekshanya Shri L
Shanney Maria Simon
Pratheeksha Shalbin

---

## 🧪 Reward Function

```python
reward = (
    revenue
    - production_cost
    - transport_cost
    - storage_cost
    - (waste * 15)
    + (satisfaction * 50)
)

