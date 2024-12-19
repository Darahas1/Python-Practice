import numpy as np

grid = [[0, 0, 3, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 8, 0, 0, 0, 7, 0, 0, 6],
        [1, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 5, 0, 0, 3, 0, 0],
        [0, 7, 0, 2, 0, 0, 0, 8, 1],
        [0, 9, 0, 6, 1, 0, 7, 0, 0],
        [3, 5, 1, 0, 9, 0, 0, 0, 0],
        [0, 6, 4, 0, 5, 0, 0, 1, 0]]

print("\nYour Input:")
print(np.matrix(grid))


def possible(row, column, number):
    # Check if number is already in the row or column
    for i in range(9):
        if grid[row][i] == number or grid[i][column] == number:
            return False

    # Check if number is in the 3x3 subgrid
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == number:
                return False
    return True


def solve():
    global grid
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:  # Find an empty space
                for number in range(1, 10):
                    if possible(row, column, number):  # Check if number is valid
                        grid[row][column] = number
                        solve()  # Recursively solve the rest
                        grid[row][column] = 0  # Backtrack if no solution found
                return  # Return if no valid number can be placed
    print("\nSolved Matrix:")
    print(np.matrix(grid)) 
    return  # Exit after finding one solution

if __name__ == '__main__':
    solve()
