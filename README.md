~~~~N-Queens Solver with Graphical User Interface
This project is a software application with a graphical user interface that solves the classic N-Queens problem using three different algorithms:

* Backtracking

* Genetic Algorithm

* Constraint Satisfaction Problem (CSP)


About the N-Queens Problem

The N-Queens problem is a classic computer science challenge where the goal is to place N queens on an N×N chessboard so that no two queens threaten each other. Queens cannot share the same row, column, or diagonal.



Project Features

* Simple and user-friendly GUI built with the Tkinter library

* Allows choosing the board size (N) freely, with a minimum of N=4

* Supports three different algorithms to solve the problem, enabling comparison of speed and performance

* Graphically displays solutions on the chessboard with appropriate color coding

* Allows browsing through multiple solutions (in Backtracking mode) using “Next” and “Previous” buttons

* Shows the genetic algorithm’s progress and status as text output in the console



Implemented Algorithms

1. Backtracking Algorithm

A depth-first recursive search method that places queens in a way that none threaten each other, finding all possible solutions.

2. Genetic Algorithm

An evolutionary optimization algorithm that uses a population of chromosomes, mutation, and crossover operators to search for the best solution. Suitable for larger board sizes and more complex problems.

3. Constraint Satisfaction Problem (CSP)

A problem-solving method that considers constraints and checks consistency (backtracking with pruning) to find solutions faster.



Project Structure

n_queen/
├── gui/
│   └── main_gui.py            
├── algorithms/
│   ├── backtracking.py       
│   ├── genetic.py           
│   └── csp.py              
├── main.py                   
└── README.md              




Important Notes

* The minimum allowed board size (N) is 4; smaller values will show a warning message.

* In Backtracking mode, all possible solutions are saved and can be viewed.

* The Genetic Algorithm and CSP methods provide only one optimized solution.

* Genetic Algorithm might take longer for larger N but is generally faster than Backtracking.

* If no perfect solution is found, the best possible solution will be displayed.~~~~