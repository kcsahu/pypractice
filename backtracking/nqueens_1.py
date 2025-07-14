def solveNQueens(n: int)-> list:
    queens = [-1 for _ in range(n)]
    return solve(0, n, queens)

def solve(row: int, n: int, queens: list)-> list:
    if row == n:
        return generate_board(n, queens)
    result = []
    for col in range(n):
        if is_valid(row, col, queens):
            queens[row] = col
            next_value = solve(row + 1, n, queens)
            if len(next_value) > 0:
                result.extend(next_value)
            queens[row] = -1
    return result
def is_valid(row: int, col: int, queens: list)-> bool:
    for prev_row in range(row):
        prev_col = queens[prev_row]
        if prev_col == col or (abs(col - prev_col) == abs(row - prev_row)):
            return False
    return True
def generate_board(n: int, queens: list)-> list:
    result = []
    for row in range(n):
        col = ['.' for _ in range(n)]
        col[queens[row]] = 'Q'
        result.append(''.join(col))
    return result

if __name__ == '__main__':
    result = solveNQueens(4)
    print(result)

