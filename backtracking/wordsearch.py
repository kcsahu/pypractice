# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
# or vertically neighboring. The same letter cell may not be used more than once.

# Input: board = [["A","B","C","E"],
#                 ["S","F","C","S"],
#                 ["A","D","E","E"]],
# word = "ABCCED"
# Output: true
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    def backtrack(row: int, col: int, index: int = 0) -> bool:
        if index == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
            return False
        tmp = board[row][col]
        board[row][col] = '$'
        result = backtrack(row + 1, col, index + 1) or \
                 backtrack(row - 1, col, index + 1) or \
                 backtrack(row, col + 1, index + 1) or \
                 backtrack(row, col - 1, index + 1)
        board[row][col] = tmp
        return result

    if board and word:
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and backtrack(row, col):
                    return True
    return False


if __name__ == "__main__":
    res = exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    print(res)
    assert res

    res = exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
    print(res)
    assert res

    res = exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    print(res)
    assert not res
