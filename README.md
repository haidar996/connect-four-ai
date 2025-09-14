# connect-four-ai
A Connect Four game implemented in Python using the Minimax algorithm with alpha-beta pruning on a 6x5 board. Includes a custom evaluation function and terminal state detection.
# Connect Four AI (6x5 Grid)

This project implements a simple yet powerful **Connect Four game AI** using the **Minimax algorithm** with **alpha-beta pruning**. It plays on a 6x5 grid (6 columns, 5 rows), and simulates intelligent decision-making by evaluating board states with a heuristic function.

>  Built in Python by **Haidar Saad**.

---

##  Features

-  6x5 Connect Four grid (custom size)
-  AI using Minimax with alpha-beta pruning
-  Custom heuristic evaluation for non-terminal states
-  Win detection in all directions: horizontal, vertical, and both diagonals
-  Simulation-ready: pre-defined test case at the bottom of the script

---

##  File Structure

| File | Description |
|------|-------------|
| `connect_four.py` | Main Python script containing all logic for the Connect Four game and AI player |

---

##  AI Details

- Uses **Minimax** algorithm with **depth-limited search (depth = 4)**
- Applies **alpha-beta pruning** for efficient performance
- Custom `evaluate()` function estimates the board's utility when the terminal state is not reached

---

##  How to Use

1. Run the script using Python 3:
   ```bash
   python connect_four.py
