import numpy as np

sudoku = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,0,0]]

def possible (row, column, number):
    global sudoku

    #check if number in row or column

    for n in range(0,9):
        if sudoku[row][n] == number:
            return False
    for n in range(0,9):
        if sudoku[n][column] == number:
            return False

    #check if number in 3x3 square

    x = (column // 3) * 3
    y = (row // 3) * 3
    for i in range(0,3):
        for p in range(0,3):
            if sudoku[y + i][x + p] == number:
                return False
    return True

def solve():
    global sudoku
    for row in range(0,9):
        for column in range(0,9):
            if sudoku[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        sudoku[row][column] = number
                        solve()
                        sudoku[row][column] = 0
                return

    print(np.matrix(sudoku))
    input('\nPress enter to try for other possible solutions')

solve()