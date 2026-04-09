# 🚀 Taycan: OpenEnv Food Supply Chain Optimization Environment

## Overview
Taycan OpenEnv is an AI-driven simulation of a food supply chain where agents optimize production, shipping, inventory, and waste reduction.  
It is built using **OpenEnv** and deployed as a **FastAPI/Docker Space** on Hugging Face.

## Features
- **Dynamic Environment:** Simulates inventory, demand, spoilage, and cost.
- **Tasks:** Three difficulty levels
  - `easy`: Stable demand, low variability
  - `medium`: Moderate demand fluctuations
  - `hard`: High uncertainty and spoilage risk
- **Endpoints:** 
  - `/reset` → Reset environment to initial state
  - `/step` → Take an action and get the next state, reward, and done flag
  - `/state` → Get current environment state
- **Evaluation:** Computes scores and rewards for AI agents.

## Installation (Local)
``bash
git clone https://github.com/Irenemalfoy/taycan-openenv-food-supply-chain.git
cd taycan-openenv-food-supply-chain
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

## 👥 Team Taycan
- Deekshanya Shri L
- Shanney Maria Simon
- Pratheeksha Shalbin 
