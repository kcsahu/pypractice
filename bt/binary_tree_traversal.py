from bt.treenode_util import TreeNodeUtil
from bt.tree_node import TreeNode
from collections import deque


## Root -> Left -> Right
def preorder_traversal(root: TreeNode) -> list[int]:
    res = []
    if root:
        stack: deque[TreeNode] = deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return res


## Left -> Root -> Right
def inorder_traversal(root: TreeNode) -> list[int]:
    res = []
    if root:
        node = root
        stack = deque()
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
    return res


## Left -> Right -> Root
def post_order_traversal(root: TreeNode) -> list[int]:
    res = deque()
    if root:
        stack = deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            res.appendleft(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    return list(res)


if __name__ == "__main__":
    root = TreeNodeUtil.build_tree([1, 2, 3, 4, 5, 6, 7])
    TreeNodeUtil.print_tree(root, "Original Tree(Level order): ")
    pre_order = preorder_traversal(root)
    print("Pre-Order traversal: ", pre_order)
    assert [1, 2, 4, 5, 3, 6, 7] == pre_order
    in_order = inorder_traversal(root)
    print("In-Order traversal: ", in_order)
    assert [4, 2, 5, 1, 6, 3, 7] == in_order
    post_order = post_order_traversal(root)
    print("Post-Order traversal: ", post_order)
    assert [4, 5, 2, 6, 7, 3, 1] == post_order
