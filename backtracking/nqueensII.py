import numpy as np

def totalNQueens(n: int)-> int:
    queens = np.full(n, -1)

    def is_valid(row, col, queens)-> bool:
        for prev_row in range(row):
            prev_col = queens[prev_row]
            if (col == prev_col) or abs(row - prev_row) == abs(col - prev_col):
                return False
        return True

    def backtrack(row:int = 0):
        if row == n:
            return 1
        total = 0
        for col in range(n):
            if is_valid(row, col, queens):
                queens[row] = col
                total += backtrack(row + 1)
                queens[row] = -1
        return total
    return backtrack()

if __name__ == "__main__":
    res = totalNQueens(4)
    print(res)
    assert res == 2