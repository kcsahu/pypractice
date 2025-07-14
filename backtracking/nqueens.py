
def solveNQueens(n : int)-> list:
    queens = [-1 for _ in range(n)]
    return solve(0, n, queens)

def is_valid(row, col, queens)-> bool:
    for prevRow in range(0, row):
        prevCol = queens[prevRow]
        if prevCol == col or (abs(row - prevRow) == abs(col - prevCol)):
            return False
    return True

def generate_board(n: int, queens: list)-> list:
    board = list()
    for row in range(0, n):
        cols = ["." for _ in range(0, n)]
        cols[queens[row]] = "Q"
        board.append(''.join(cols))
    return board


def solve(row: int, n: int, queens: list) -> list:
    if row == n:
        return generate_board(n, queens)
    result = []
    for col in range(0, n):
        if is_valid(row, col, queens):
            queens[row] = col
            board = solve(row + 1, n, queens)
            if len(board) > 0:
                result.extend(board)
            queens[row] =  -1
    return result

def solveNQueensII(n: int)-> int:
    queens = [-1 for _ in range(n)]
    result = solveII(0,n, queens)
    return result

def solveII(row: int, n: int, queens)-> int:
    if row == n:
        return 1
    res = 0
    for col in range(n):
        if is_valid(row, col, queens):
            queens[row] = col
            res += solveII(row + 1, n, queens)
            queens[row] = -1
    return res


if __name__ == "__main__":
   res = solveNQueens(4)
   print(res)

   res = solveNQueensII(4)
   print(res)