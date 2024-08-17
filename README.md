# 🧩 Maze Solver Project

Welcome to the **Maze Solver** project! This repository contains a Python implementation of various search algorithms to solve a maze represented as a 2D grid. The project allows you to explore and compare different pathfinding techniques.

## 📜 Project Overview

The Maze Solver project demonstrates the application of both heuristic and non-heuristic search algorithms to navigate through a maze. Users can choose from the following algorithms:

- **🔍 Depth-First Search (DFS)**
- **🔍 Breadth-First Search (BFS)**
- **🌐 Uniform Cost Search (UCS)**
- **⭐ A* Search**
- **💡 Best-First Search**

The maze is visualized in the console, with the solution path highlighted, allowing for easy comparison of the algorithms' efficiency and effectiveness.

## 🚀 Features

- **User-Friendly Interface**: Simple console-based interface to select the desired search algorithm.
- **Algorithm Visualization**: Visual representation of the maze and the path found by the selected algorithm.
- **Modular Codebase**: Well-organized Python scripts, each dedicated to a specific algorithm.

## 🧠 Algorithms

### Heuristic Algorithms
- **A* Search**: Combines the cost to reach a node with the estimated cost to the goal (using Manhattan distance).
- **Best-First Search**: Expands the node closest to the goal based on the Manhattan distance heuristic.

### Non-Heuristic Algorithms
- **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking.
- **Breadth-First Search (BFS)**: Explores all nodes at the current depth level before moving deeper.
- **Uniform Cost Search (UCS)**: Expands the least-cost node, ensuring the shortest path in an unweighted graph.

## 📂 Project Structure

## 🔧 How to Run

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/maze-solver.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd maze-solver
    ```
3. **Run the main script**:
    ```bash
    python main.py
    ```
4. **Choose your desired algorithm** and watch the maze get solved!

## ✨ Example Output

```bash
1 1 1 1 1 1 
1 # # # # 1 
1 # 1 1 # 1 
1 # 1 # # 1 
1 # 1 # 1 1 
1 # # # # 1 
1 1 1 1 1 1






