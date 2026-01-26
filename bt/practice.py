from tree_node import TreeNode
from collections import deque
from treenode_util import TreeNodeUtil
## Pre-Order: Root -> Left -> Right
def pre_order(root: TreeNode)-> list:
    result = []
    if root:
        stack = deque([root])
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return result
## In-Order: Left -> Root -> Right
def in_order(root: TreeNode)->list:
    result = []
    if root:
        stack = deque()
        node: TreeNode = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
    return result
                

## Post-Order: Left -> Right -> Root
def post_order(root: TreeNode) -> list:
    result = []
    if root:
        dq = deque()
        stack = deque([root])
        while stack:
            node = stack.pop()
            dq.appendleft(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        result = list(dq)
    return result

def build_tree(arr: list, index: int = 0)-> TreeNode:
    if index < len(arr):
        node = TreeNode(arr[index])
        left = (index <<1 )+1
        right = (index << 1) + 2
        node.left = build_tree(arr, left)
        node.right = build_tree(arr, right)
        return node
    return None

def is_symmetry(root: TreeNode) -> bool:
    def is_mirror(left_node, right_node)-> bool:
        if left_node and right_node:
            val = left_node.val == right_node.val
            val = val and (is_mirror(left_node.left, right_node.right) 
                           and is_mirror(left_node.right, right_node.left))
            return val
        elif left_node == right_node:
            return True
        else: 
            return False
    if root:
        return is_mirror(root.left, root.right)  
    return False



if __name__ == "__main__":
    root = TreeNodeUtil.build_tree([1,2,2,3,4,4,3])
    res = is_symmetry(root)
    print(res)

    root = TreeNodeUtil.build_tree([1, 2, 3, 4, 5, 6, 7])
    TreeNodeUtil.print_tree(root, "Original Tree(Level order): ")
    result = pre_order(root)
    print("Pre-Order traversal: ", result)
    assert [1, 2, 4, 5, 3, 6, 7] == result

    result = post_order(root)
    print("Post-Order traversal: ", result)
    assert [4, 5, 2, 6, 7, 3, 1] == result

    result = in_order(root)
    print("In-Order traversal: ", result)
    assert [4, 2, 5, 1, 6, 3, 7] == result

    root = build_tree([1,2,3,4,5,6,7])
    TreeNodeUtil.print_tree(root)
