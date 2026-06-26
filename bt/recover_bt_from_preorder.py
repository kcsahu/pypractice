from tree_node import TreeNode
from treenode_util import TreeNodeUtil
from collections import deque


class Solution:

    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        i = 0
        tlen = len(traversal)
        stack = deque()
        while i < tlen:
            depth = 0
            while i < tlen and traversal[i] == "-":
                i += 1
                depth += 1
            val = 0
            while i < tlen and traversal[i] != '-':
                val = val * 10 + int(traversal[i])
                i += 1

            node = TreeNode(val)
            while len(stack) > depth:
                stack.pop()

            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]


if __name__ == "__main__":
    traversal = "1-2--3--4-5--6--7"
    sol = Solution()
    root = sol.recoverFromPreorder(traversal)
    TreeNodeUtil.print_tree(root)
    root = sol.recoverFromPreorder("1-2--3---4-5--6---7")
    TreeNodeUtil.print_tree(root)
    root = sol.recoverFromPreorder("1-401--349---90--88")
    TreeNodeUtil.print_tree(root)
