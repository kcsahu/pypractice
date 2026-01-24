
from tree_node import TreeNode
from treenode_util import TreeNodeUtil
def recover_tree(preorder:list)-> TreeNode:
    index = 0
    def build_tree()->TreeNode:
        nonlocal index
        if preorder[index] == None:
            index += 1
            return None
        node = TreeNode(preorder[index])
        index += 1

        node.left = build_tree()
        node.right = build_tree()

        return node
    return build_tree()

if __name__ == "__main__":
    preorder = [1,2,None, None,3,4,None, None,5,None,None]
    root = recover_tree(preorder)
    TreeNodeUtil.print_tree(root)