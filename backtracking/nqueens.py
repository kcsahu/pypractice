def solveNQueens(n: int)-> list[list[int]]:
    queens = [-1] * n
    result = []

    def backtrack(row: int = 0):
        if row == n:
            result.append(__generate_board(n, queens))
            return
        for col in range(n):
            if __is_valid(row, col, queens):
                queens[row] = col
                backtrack(row + 1)
                queens[row] = - 1

    backtrack()
    return result

def __is_valid(row, col, queens)-> bool:
     for prev_row in range(row):
         prev_col = queens[prev_row]
         if (col == prev_col) or (abs(col - prev_col) == abs(row - prev_row)):
             return False
     return True

def __generate_board(n, queens)-> list:
    board = []
    for row in range(n):
        cols = ['.'] * n
        cols[queens[row]] = 'Q'
        board.append(''.join(cols))
    return board


if __name__ == "__main__":
   res = solveNQueens(4)
   print(res)
   assert res == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
