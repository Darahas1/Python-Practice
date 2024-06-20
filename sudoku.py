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

print(np.matrix(grid))


def possible(row, column, number):
    global grid
    for i in range(0,9):
        if grid[row] [i] == number:
            return False
        
        for i in range(0,9):
            if grid[i] [row] == number:
                return False
            
            x0 = (column // 3) * 3
            y0 = (row // 3) * 3
            for i in range(0,3):
                for j in range(0,3):
                    if grid[y0+i] [x0+j] == number:
                        return False
                    
            return True
def solve():
    global grid
    for row in range(0,9):
        for column in  range(0,9):
            if grid[row] [column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row] [column] = number
                        solve()
                        grid[row] [column] = 0
                return
    print(np.matrix(grid))
    input('More possible solutions')

solve()