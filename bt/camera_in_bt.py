# You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, 
# itself, and its immediate children.

# Return the minimum number of cameras needed to monitor all nodes of the tree.
from tree_node import TreeNode
from collections import deque
from treenode_util import TreeNodeUtil

class Solution:
    def minCameraCover(self, root: TreeNode)-> int:
        ## 3 states
        # 0 - Not covered. Node needs a camera from its parent
        # 1 - Covered. Node has its own camera
        # 2 - Node is covered by a child camera.
        self.cameras = 0
        def dfs(node: TreeNode)-> int:
            if not node:
                return 2
            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                self.cameras += 1
                return 1

            if left == 1 or right == 1:
                return 2
            
            return 0
        if dfs(root) == 0:
            self.cameras += 1
        return self.cameras



    
if __name__ == "__main__":
    root = TreeNodeUtil.build_tree([1,2,None,3,4])
    sol = Solution()
    res = sol.minCameraCover(root)
    print(res)
    # assert res == 1
    root = TreeNodeUtil.build_tree([0,0,0,0,0,0,0])
    print(sol.minCameraCover(root))

    # root = TreeNodeUtil.build_tree([0,0,None,0,None,0,None,None,0])
    # print(sol.minCameraCover(root))


