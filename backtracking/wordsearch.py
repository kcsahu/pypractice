from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board) == 0 or not word or len(word) == 0:
            return False
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and self.solve(row, col, board, word, 0):
                    return True
        return False

    def solve(self, row: int, col: int, board: List[List[str]], word: str, index: int) -> bool:
        if index == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or \
               word[index] != board[row][col]:
            return False

        tmp = board[row][col]
        board[row][col] = '$'
        result = self.solve(row + 1, col, board, word, index + 1) or \
                 self.solve(row - 1, col, board, word, index + 1) or \
                 self.solve(row, col + 1, board, word, index + 1) or \
                 self.solve(row, col - 1, board, word, index + 1)
        board[row][col] = tmp
        return result


if __name__ == "__main__":
    obj = Solution()
    res = obj.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    print(res)
    assert res
    res = obj.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    print(res)
    assert res