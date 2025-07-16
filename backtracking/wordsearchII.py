from typing import List


class TrieNode:
    child: dict[str, 'TrieNode'] = None
    is_end: bool
    word: str

    def __init__(self):
        self.child = dict()
        self.is_end = False


class Solution:
    root: TrieNode = TrieNode()

    def build_trie(self, words: list):
        for word in words:
            node = self.root
            for w in word:
                next_node = node.child.get(w, None)
                if not next_node:
                    next_node = TrieNode()
                node.child[w] = next_node
                node = next_node
            node.is_end = True
            node.word = word

    def findWords(self, board: List[List[str]], words: List[str]):
        self.build_trie(words)
        rows = len(board)
        cols = len(board[0])
        result = []
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in self.root.child.keys():
                    self.solve(row, col, board, self.root, result)
        return result

    def solve(self, row, col, board, node: TrieNode, result: list):
        if node.is_end:
            result.append(node.word)
            node.is_end = False
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False
        tmp = board[row][col]
        board[row][col] = '$'
        node = node.child.get(tmp, None)
        is_found = False
        if node:
            is_found = (self.solve(row + 1, col, board, node, result)
                        or self.solve(row - 1, col, board, node, result)
                        or self.solve(row, col + 1, board, node, result)
                        or self.solve(row, col - 1, board, node, result))
        board[row][col] = tmp
        return is_found


if __name__ == "__main__":
    obj = Solution()
    res = obj.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                        ["oath", "pea", "eat", "rain"])
    print(res)
    assert ['oath', 'eat'] == res

    res = obj.findWords([["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]],
                        ["oa", "oaa"])
    print(res)
    assert ['oa', 'oaa'] == res
