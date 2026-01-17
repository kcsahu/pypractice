from tree_node import TreeNode
from treenode_util import TreeNodeUtil
from collections import deque


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
    assert res

    root = TreeNodeUtil.build_tree([1,2,2,None,3,None,3])
    TreeNodeUtil.print_tree(root)
    res = is_symmetry(root)
    print(res)
    assert not res