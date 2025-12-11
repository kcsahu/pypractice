
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left : TreeNode = None
        self.right : TreeNode = None

    def __str__(self):
        return str(self.val)