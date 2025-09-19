from collections import deque

from bt.treenode_util import TreeNode
from bt.treenode_util import *


def pre_order_traversal(root: TreeNode)-> list[int]:
    result = []
    if root:
        dq = deque()
        dq.append(root)
        while len(dq) > 0:
            node = dq.pop()
            result.append(node.val)
            if node.right:
                dq.append(node.right)
            if node.left:
                dq.append(node.left)
    return result

def post_order_traversal(root: TreeNode)-> list[int]:
    result = deque()
    if root:
        dq = deque()
        dq.append(root)
        while dq:
            node = dq.pop()
            result.appendleft(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
    return list(result)

if __name__=="__main__":
    root = build_tree([1,2,3,4,5,6,7], 0)
    traversed = pre_order_traversal(root)
    print_tree(root, "Actual Binary Tree: ")
    print("Pre-order Traversal: ",traversed)
    assert [1, 2, 4, 5, 3, 6, 7] == traversed
    traversed = post_order_traversal(root)
    print("Post-order Traversal: ", traversed)
    assert [4, 5, 2, 6, 7, 3, 1] == traversed