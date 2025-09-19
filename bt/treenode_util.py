from collections import deque
import numpy as np

class TreeNode:

    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)



def build_tree(arr: list, index: int)-> TreeNode:
   if index < len(arr):
       node = TreeNode(arr[index])
       left = (index<<1) + 1
       node.left = build_tree(arr, left)
       right = (index<<1) + 2
       node.right = build_tree(arr,right)
       return node
   return None

def print_tree(root: TreeNode, msg: str=None):
    res = []
    if root:
        dq = deque()
        dq.append(root)
        while len(dq) > 0:
            node = dq.popleft()
            res.append(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
    msg = msg if msg else ''
    print(msg, res)

if __name__ =="__main__":
    arr = [2,4,6,8,1,5,9]
    root = build_tree(arr, 0)
    print_tree(root)






