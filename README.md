# Markov Decision Process (MDP) Reinforcement Learning Implementation in Python

**Author:** Leo Martinez III - [LinkedIn](https://www.linkedin.com/in/leo-martinez-iii/)

**Contact:** [leo.martinez@students.tamuk.edu](mailto:leo.martinez@students.tamuk.edu)

**Created:** Spring 2024

---

## Overview:
This project implements a Markov Decision Process (MDP) using Reinforcement Learning in Python. The code performs value iteration to compute the utility values for each state in a grid. The objective is to find the optimal policy for the agent to maximize its expected reward over time.

## Features:
- **Grid Setup:** A 5x5 grid with specified terminal and blocked states.
- **Actions:** The agent can move in four directions: up, down, left, and right.
- **Rewards:** Each state transition incurs a reward of -0.5, except for terminal states with fixed rewards.
- **Discount Factor:** The discount factor (γ) is set to 0.9, determining the importance of future rewards.
- **Value Iteration:** The utility values for each state are updated iteratively based on the Bellman equation.
- **Iterations:** The value iteration process is demonstrated for different numbers of iterations: 5, 10, 15, 20, 50, and 100.

## Repository Structure:
- **src:** Contains the Python source code for the program.
- **README.md:** Provides context and information about the project (you're currently reading it!).
- **LICENSE:** Includes license information (MIT) for the GitHub repository.

# Note:
- This program was written in Spyder IDE using Python 3.18
