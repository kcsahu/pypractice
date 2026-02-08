import numpy as np

def totalNQueens(n: int)-> int:
    queens = np.full(n, -1)
    total_queens = 0

    def is_valid(row, col, queens)-> bool:
        for prev_row in range(row):
            prev_col = queens[prev_row]
            if (col == prev_col) or abs(row - prev_row) == abs(col - prev_col):
                return False
        return True

    def backtrack(row:int = 0):
        if row == n:
            nonlocal total_queens
            total_queens += 1    
            return
        for col in range(n):
            if is_valid(row, col, queens):
                queens[row] = col
                backtrack(row + 1)
                queens[row] = -1
    
    backtrack()
    return total_queens

if __name__ == "__main__":
    res = totalNQueens(4)
    print(res)
    assert res == 2