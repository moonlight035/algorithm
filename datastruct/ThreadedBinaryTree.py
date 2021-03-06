#线索二叉树,只有中序是完善的
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.lflag = 0
        self.right = None
        self.rflag = 0

class ThreadedBinaryTree:

    def makeTree(self, root: TreeNode):
        def done(node: TreeNode):
            global pre
            if node:
                done(node.left)
                if not node.left:
                    node.lflag = 1
                    node.left = pre
                if pre and not pre.right :
                    pre.rflag = 1
                    pre.right = node
                pre = node
                done(node.right)
        done(root)

    def LNR(self, root: TreeNode):
        t = root
        while t.lflag == 0:
            t = t.left
        res = []
        while t:
            res.append(t.val)
            if t.rflag == 0:
                t = t.right
                while t and t.lflag == 0:
                    t = t.left
            else:
                t = t.right
        return res

    def makeNLRTree(self, root: TreeNode):
        def done(node: TreeNode):
            global pre
            if node:
                if not node.left:
                    node.lflag = 1
                    node.left = pre
                if pre and not pre.right :
                    pre.rflag = 1
                    pre.right = node
                pre = node
                if node.lflag == 0:
                    done(node.left)
                done(node.right)
        done(root)
    def NLR(self, root: TreeNode):
        t = root
        res = []
        while t:
            res.append(t.val)
            if t.rflag == 1:
                t = t.right
            elif t.lflag == 0:
                t = t.left
            else:
                t = t.right
        return res




pre = None
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(10)
root.left.right = TreeNode(12)
root.right.left = TreeNode(8)
root.right.right = TreeNode(9)
t = ThreadedBinaryTree()
t.makeNLRTree(root)
print(t.NLR(root))

pre = None
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(10)
root.left.right = TreeNode(12)
root.right.left = TreeNode(8)
root.right.right = TreeNode(9)
t = ThreadedBinaryTree()
t.makeTree(root)
print(t.LNR(root))

# 5 4 10 12 3 8 9
# 10 4 12 5 8 3 9

