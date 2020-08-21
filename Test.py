class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.lflag = 0
        self.right = None
        self.rflag = 0


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(10)
root.left.right = TreeNode(12)
root.right.left = TreeNode(8)
root.right.right = TreeNode(9)
