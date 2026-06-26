import numpy as np

def longestIncreasingPath(matrix) -> list:
    if not matrix or not matrix[0]:
        return []
    rows, cols = len(matrix), len(matrix[0])
    dp = [[None] * cols for i in range(rows)]
    direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(row, col)-> list:
        if dp[row][col] != None:
            return dp[row][col]
        longest_seq = [matrix[row][col]]
        for dx, dy in direction:
            x, y = dx + row, dy + col
            if 0<= x < rows and 0<= y < cols and matrix[x][y] > matrix[row][col]:
                seq: list = dfs(x, y)
                longest_seq = longest_seq + seq if len(seq) + 1 > len(longest_seq) else longest_seq
        dp[row][col] = longest_seq
        return longest_seq

    longest_seq = []
    for row in range(rows):
        for col in range(cols):
            seq = dfs(row, col)
            longest_seq = seq if len(seq) > len(longest_seq) else longest_seq
    return longest_seq


if __name__ == "__main__":
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    res = longestIncreasingPath(matrix)
    print(res)
