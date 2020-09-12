# Sudoku Solver
This is a basic implementation of a Sudoku Solver, using a backtrack algorithm. Currently only prints out the sudoku fields inside the terminal.

## How to use it?
Input your sudoku field in form of a 2D-array and call the `solve()` function with your 2D-array as a argument. After the function call you can print your sudoku field and it should be solved. If the sudoku was solved or not can be checked by printing out the return value of `solve()`. When the value is `True` the sudoku was solvable, otherwise you will receive a error message which indicates some kind of recursion overflow.
