import numpy as np

# define a sudoku grid to solve 
sudoku_easy =    [[4, 0, 9, 0, 0, 8, 0, 0, 6],
                  [0, 2, 0, 6, 0, 9, 1, 0, 3],
                  [0, 0, 0, 2, 0, 0, 9, 0, 8],
                  [0, 0, 2, 0, 6, 3, 0, 1, 0],
                  [0, 0, 0, 0, 7, 0, 6, 5, 9],
                  [0, 1, 7, 0, 0, 0, 0, 0, 2],
                  [9, 0, 0, 0, 0, 0, 7, 6, 5],
                  [3, 7, 1, 0, 0, 0, 0, 0, 0],
                  [0, 5, 6, 8, 4, 7, 0, 0, 0]] 

sudoku_hard =    [[0, 0, 1, 2, 0, 7, 0, 0, 0],
                  [0, 6, 2, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 9, 4, 0],
                  [0, 0, 0, 9, 8, 0, 0, 0, 3],
                  [5, 0, 0, 0, 0, 0, 0, 0, 0],
                  [7, 0, 0, 0, 3, 0, 0, 2, 1],
                  [0, 0, 0, 1, 0, 2, 0, 0, 0],
                  [0, 7, 0, 8, 0, 0, 4, 1, 0],
                  [3, 0, 4, 0, 0, 0, 0, 8, 0]] 

def empty(sudo):
    for y in range(9):
        for x in range(9):
            if sudo[y][x] == 0:
                return y, x
    return None

def check(sudo, x, y, n):
    
    # check column (Spalte)
    for i in range(9):
        if sudo[i][x] == n and y != i:
            return False

    # check row (Zeile)
    for i in range(9):
        if sudo[y][i] == n and x != i:
            return False
    
    # check in which x coordinate we need to start
    if x/3 < 1:
        addx = 0
    elif x/3 >= 1 and x/3 < 2:
        addx = 3
    else: 
        addx = 6

    # check in which y coordinate we need to start
    if y/3 < 1:
        addy = 0
    elif y/3 >= 1 and y/3 < 2:
        addy = 3
    else: 
        addy = 6

    # check 3x3 square
    for i in range(addx, 3+addx):
        for j in range(addy, 3+addy):
            if sudo[j][i] == n:
                return False
    
    return True

def solve(sudo):
    
    # first of all check if there are any empty fields

    # if there are no empty fields it means we solved the sudoku -> return true!
    if empty(sudo) == None:
        return True

    # otherwise we need find the y and x coordinate inside the array
    else:
        y, x = empty(sudo) 
    
    # then go through all possible numbers "n" (number between 1-9) and
    # check if the number "n" is valid. When the first valid number n is found,
    # set this number to the coordinates y and x. After that call the 
    # solve function recursively and repeat the process. When a possible solution
    # is found return true, otherwise reset the last set solution. When a number is 
    # reseted, the for loop will go to the next higher number which could fit into 
    # the given x and y coordinate
    for n in range(1, 10):
        if check(sudo, x, y, n):
            sudo[y][x] = n

            if solve(sudo):
                return True
            else:
                sudo[y][x] = 0
    return False

# prints sudoku field before solving it
print(np.matrix(sudoku_hard))
print("---------------------")

# solve given field
solve(sudoku_hard)

# print out solution
print(np.matrix(sudoku_hard))