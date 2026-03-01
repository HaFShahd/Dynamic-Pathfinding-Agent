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


## Screenshots

<img width="1146" height="752" alt="image" src="https://github.com/user-attachments/assets/093942d0-3283-4b70-8297-0d8e0f3d4a13" />

## Requirements

- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)
- Standard libraries: random, time, heapq, math


## Installation

1. **Install Python 3** if not already installed:

   - [Python Downloads](https://www.python.org/downloads/)

2. **Install Tkinter** (if not included in your Python installation):

pip install tk

3. **Clone or download the repository**:

git clone <your-repository-url>
cd <repository-folder>

## Running the Application

1. Open a terminal or command prompt.
2. Navigate to the folder containing Dynamic_Pathfinding.py.
3. Run the program:

python Dynamic_Pathfinding.py

## Usage Instructions

1. **Grid Size & Density:**

   * Enter the number of **Rows** and **Columns**.
   * Enter the **Density %** for random obstacles (e.g., 30 for 30% wall coverage).

2. **Random Map Generation:**

   * Click the **Random Map** button to generate the grid.

3. **Edit Mode:**

   * **Draw Walls:** Click on the grid to place/remove obstacles.
   * **Set Start / Goal:** Click the respective button and then click a cell to move Start/Goal.

4. **Algorithm & Heuristic:**

   * Choose **A*** or **GBFS**.
   * Choose **Manhattan** or **Euclidean** distance.

5. **Dynamic Obstacles:**

   * Click **Toggle Dynamic** to enable or disable dynamic obstacle spawning during the agent’s movement.

6. **Start Search:**

   * Click **Start Search** to let the agent find a path.
   * Watch the visualization: yellow = frontier, blue = visited, green = final path, cyan = agent position.

7. **Metrics:**

   * After reaching the goal, the dashboard shows:

     * **Nodes Visited**
     * **Path Cost**
     * **Execution Time** in milliseconds.


