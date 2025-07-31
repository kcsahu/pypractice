

# matrix:
# [o a a n]
# [e t a e]
# [i h k r]
# [i f i v]
#
# words: ["oath", "pea", "eat", "rain"]

from typing import List
import numpy as np

class TrieNode:

    word: str

    def __init__(self):
        self.child = dict()
        self.is_end = None

class Solution:

    root: TrieNode = TrieNode()

    def build_trie(self, words: List[str]):
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

    def find_words(self, matrix: List[List[str]], words: List[str])-> List[str]:
        self.build_trie(words)
        matrix = np.array(matrix)
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] in self.root.child.keys():
                    self.solve(row, col, matrix, self.root, result)
        return result

    def solve(self, row: int, col: int, matrix, node: TrieNode, result: list):
        if node.is_end:
            node.is_end = False
            result.append(node.word)
            return True
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return False
        tmp = matrix[row][col]
        matrix[row][col] = '$'
        node = node.child.get(tmp, None)
        is_found = False
        if node:
            is_found = (self.solve(row + 1, col, matrix, node, result)
            or self.solve(row - 1, col, matrix, node, result)
            or self.solve(row, col + 1, matrix, node, result)
            or self.solve(row, col - 1, matrix, node, result))
        matrix[row][col] = tmp
        return is_found

if __name__ == "__main__":
    obj = Solution()
    res = obj.find_words([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                        ["oath", "pea", "eat", "rain"])
    print(res)
    assert ['oath', 'eat'] == res