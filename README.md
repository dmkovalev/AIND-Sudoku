# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: We are searching for pairs of values in unitlist. After that, for each unit
in unitlist naked twins values are removed from corresponding boxes in the
units. This is possible since those values can not be in that boxes - that
would lead to inconsistent board. This is constraint propagation.

Naked twins strategy works as follows. If we have two boxes in the same unit
with same values 'xy', it becomes possible to exclude digits x and y from other
boxes in the unit. This is possible, because if not true, for example 'x' exists
in other cell, then x can be excluded from naked twins, which leads to single
digit 'y' as value in two cells in the unit. Since it starts to break constraints and brings to inconsistency, it is a constraint propagation.


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: We add diagonal unit to unitlist and eliminate, naked_twins and only_choice
use it during their checks.

Constraint propagation is the general term for propagating the implications of
a constraint on one variable onto other variables (from ref). Diagonal sudoku
is solved with recursive applicatio of naked_twins, eliminate and only_choice
implementations of constraint propagation rules and search. Naked twins is
decribed above. 

Elimination works as follows. If a box has some value 'x', then no other boxes
in a box's peers can have this value.

Only choice works as follows. If exists just one box in a unit, which can be
assigned just a single value, then it must be assigned this value.

If following constraint propagation rules leave multiple values, then we start
to do search, which means assigning of the possible values and recursively
applying constraint propagation.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
