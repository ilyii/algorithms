"""
A sudoku solver.
"""
import cv2
import numpy as np

def validate(sudoku, row, col, num):
    """
    Check if a number is valid in a cell.
    """
    # Check row
    if num in sudoku[row,:]:
        return False
    # Check column
    if num in sudoku[:,col]:
        return False
    # Check 3x3 square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in sudoku[start_row:start_row+3, start_col:start_col+3]:
        return False
    return True


def visualize(sudoku):
    """
    Visualize the sudoku.
    """

    print(20*"-")
    for row in sudoku:
        print(row)


def solve(sudoku):
    """
    (1) Find an empty cell.
    (2) Try all numbers from 1 to 9.
    (3) If a number is valid, assign it to the cell.
    (4) Repeat the process.
    """
    w,h = sudoku.shape
    empty = None
    for i in range(w):
        for j in range(h):
            if sudoku[i,j] not in range(1,10): # Not assigned
                empty = i,j

    if not empty:
        return True
    
    row, col = empty

    for num in range(1,10):
        if validate(sudoku, row, col, num):
            sudoku[row, col] = num
            if solve(sudoku):
                return True
            sudoku[row, col] = 0

    return False


if __name__ == "__main__":
  
    SUDOKU = np.array([
        [0,0,0,0,0,8,4,9,7],
        [0,0,4,9,0,7,1,5,0],
        [0,0,7,0,0,0,2,3,0],
        [0,0,0,0,7,0,6,0,0],
        [0,7,0,3,4,0,0,0,0],
        [0,0,3,0,5,9,8,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,4,9],
        [6,0,5,7,9,0,0,0,0]
    ])

    visualize(SUDOKU)
    solve(SUDOKU)
    visualize(SUDOKU)


