# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

# For each node at position (row, col), its left and right children will be at 
# positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for 
# each column index starting from the leftmost column and ending on the rightmost column. 
# There may be multiple nodes in the same row and same column. In such a case, 
# sort these nodes by their values.

# Return the vertical order traversal of the binary tree.

from tree_node import TreeNode
from treenode_util import TreeNodeUtil
from collections import defaultdict, deque

def verticalTraversal(root: TreeNode)->list[list[int]]:
    ## BFS - Level order. Sort the values at Row level
    if root:
        graph = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            qsize = len(queue)
            row_list = []
            for i in range(qsize):
                node_t = queue.pop()
                if node_t[0].val is not None:
                    row_list.append(node_t)
                if node_t[0].left:
                    queue.appendleft((node_t[0].left, node_t[1] - 1))
                if node_t[0].right:
                    queue.appendleft((node_t[0].right, node_t[1] + 1))
            sorted_row = sorted(row_list, key = lambda x: x[0].val)
            for item in sorted_row:
                graph[item[1]].append(item[0].val)
            
    if graph:
        return [graph[k] for k in sorted(graph.keys())]
    return []
    
if __name__ == "__main__":
    root = TreeNodeUtil.build_tree([1,2,3,4,6,5,7])
    res = verticalTraversal(root)
    print(res)
    assert [[4], [2], [1, 5, 6], [3], [7]] == res

    root = TreeNodeUtil.build_tree([3,9,20,None,None,15,7])
    res = verticalTraversal(root)
    print(res)
    assert [[9], [3, 15], [20], [7]] == res

    root = TreeNodeUtil.build_tree([3,1,4,0,2,2])
    res = verticalTraversal(root)
    print(res)
    assert [[0], [1], [3, 2, 2], [4]] == res
                



