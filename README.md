# Dynamic Pathfinding Agent

## Project Overview
This project implements a **Dynamic Pathfinding Agent** that navigates a grid-based environment using **Informed Search Algorithms**. The agent can handle dynamically appearing obstacles while in motion, requiring **real-time path detection and re-planning**.

The agent supports the following features:
- **Dynamic Grid Sizing:** Users can define the number of rows and columns.
- **Fixed Start & Goal:** Start and Goal nodes are clearly defined and can be moved manually.
- **Random Map Generation:** Generate random maps with user-defined obstacle density.
- **Interactive Map Editor:** Place or remove obstacles by clicking on the grid.
- **Search Algorithms:** Choose between **A*** or **Greedy Best-First Search (GBFS)**.
- **Heuristics:** Choose between **Manhattan** and **Euclidean** distance.
- **Dynamic Obstacles:** Obstacles can appear randomly while the agent moves, triggering automatic re-planning.
- **Real-Time Visualization:** Shows frontier nodes (yellow), visited nodes (blue), current agent position (cyan), and final path (green).
- **Metrics Dashboard:** Displays nodes visited, path cost, and execution time.

---

## Screenshots

<img width="1146" height="752" alt="image" src="https://github.com/user-attachments/assets/093942d0-3283-4b70-8297-0d8e0f3d4a13" />

## Requirements

- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)
- Standard libraries: `random`, `time`, `heapq`, `math`

---

## Installation

1. **Install Python 3** if not already installed:

   - [Python Downloads](https://www.python.org/downloads/)

2. **Install Tkinter** (if not included in your Python installation):

```bash
pip install tk
