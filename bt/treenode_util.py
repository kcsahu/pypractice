from collections import deque

from bt.tree_node import TreeNode


class TreeNodeUtil:

    ## 1->2->3->4->5->6
    @staticmethod
    def build_tree(arr: list, index: int = 0) -> TreeNode:
        if index < len(arr):
            root = TreeNode(arr[index])
            left_index = (index << 1) + 1
            right_index = (index << 1) + 2
            root.left = TreeNodeUtil.build_tree(arr, left_index)
            root.right = TreeNodeUtil.build_tree(arr, right_index)
            return root
        return None

    @staticmethod
    def print_tree(root: TreeNode, msg: str = ''):
        res = []
        if root:
            dq: deque[TreeNode] = deque()
            dq.appendleft(root)
            while dq:
                node = dq.pop()
                res.append(node.val)
                if node.left:
                    dq.appendleft(node.left)
                if node.right:
                    dq.appendleft(node.right)
        res_str = '->'.join(str(item) for item in res)
        print(msg, res_str)
