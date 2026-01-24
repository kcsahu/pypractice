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
    m, n = len(matrix), len(matrix[0])
    # dp = [[0] * n for i in range(m)]
    dp = np.zeros((n, m), dtype=np.int64)

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def dfs(i, j):
        if dp[i,j] != 0:
            return dp[i,j]
        longest = 1
        for (dx, dy) in direction:
            x, y = i+dx, j+dy
            if 0 <= x < m and 0<= y < n and matrix[x][y] > matrix[i][j]:
                longest = max(longest, 1 + dfs(x, y))
        dp[i][j] = longest
        return longest        

    longest = 0
    for i in range(m):
        for j in range(n):
            longest = max(longest, dfs(i, j))
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
