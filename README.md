# Robot-Pathfinding-Puzzle

This project implements a robot navigation puzzle in a 2x2 grid, where the robot moves from a Start position to an End goal while avoiding blocked cells. The robot can move up or right but must navigate around restricted cells.

Project Overview
The puzzle is modeled as a class, Puzzle, that:

Defines moves within the grid.
Randomly generates move sequences.
Utilizes uninformed search algorithms to find paths.

Features
Puzzle Class: Manages state transitions and validates moves.
Randomized Play Method: Generates a sequence of moves.

Search Algorithms:
Depth-First Search (DFS)
Breadth-First Search (BFS)
Depth-Limited Search
Iterative Deepening Search (IDS)

Run puzzle.py for the main puzzle and search algorithms.
