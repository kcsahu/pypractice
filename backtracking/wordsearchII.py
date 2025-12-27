
class TrieNode:

    def __init__(self):
        self.child = {}
        self.is_end = False
        self.word: str = None

class Solution:
    def __init__(self):
        self.root = TrieNode()
    def __build_trie(self, words: list[str]):
        for word in words:
            node: TrieNode = self.root
            for w in word:
                next_node = node.child.get(w, None)
                if not next_node:
                    next_node = TrieNode()
                    node.child[w] = next_node
                node = next_node
            node.is_end = True
            node.word = word

    def findWords(self, board: list[list[str]], words: list[str])-> list:
        result = []
        def backtrack(row: int, col: int, node: TrieNode):
            if node and node.is_end:
                node.is_end = False
                result.append(node.word)
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return
            tmp = board[row][col]
            board[row][col] = '#'
            node = node.child.get(tmp, None)
            if node:
                backtrack(row + 1, col, node)
                backtrack(row - 1, col, node)
                backtrack(row, col + 1, node)
                backtrack(row, col - 1, node)
            board[row][col] = tmp

        if board and words:
            self.__build_trie(words)
            rows = len(board)
            cols = len(board[0])
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] in self.root.child.keys():
                        backtrack(row, col, self.root)
        return result

if __name__ == "__main__":
    obj = Solution()
    res = obj.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                         ["oath", "pea", "eat", "rain"])
    print(res)
    assert ['oath', 'eat'] == res

    res = obj.findWords([["a","b"],["c","d"]], ["abcb"])
    print(res)
    assert [] == res

    res = obj.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
                        # ["hklf","hf"]
                        ["oath","pea","eat","rain","hklf", "hf"]
                        )
    print(res)
    assert res == ['oath', 'eat', 'hf', 'hklf']