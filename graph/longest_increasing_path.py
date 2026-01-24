# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may 
# not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

import numpy as np

def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    # dp = [[0] * cols for i in range(rows)]
    dp = np.zeros((rows, cols), dtype=np.int64)

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def dfs(row, col):
        if dp[row][col] != 0:
            return dp[row][col]
        longest = 1
        for (dx, dy) in direction:
            x, y = row+dx, col+dy
            if 0 <= x < rows and 0<= y < cols and matrix[x][y] > matrix[row][col]:
                longest = max(longest, 1 + dfs(x, y))
        dp[row][col] = longest
        return longest        

    longest = 0
    for row in range(rows):
        for col in range(cols):
            longest = max(longest, dfs(row, col))
    return longest

if __name__ == "__main__":
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    res = longestIncreasingPath(matrix)
    print(res)
    assert res == 4

    res = longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])
    print(res)
    assert res == 4

    res = longestIncreasingPath([[1]])
    print(res)
    assert res == 1
