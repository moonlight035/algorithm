class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MorrisTraversal:

    #先序
    def NLR(self, root: TreeNode):
        cur = root
        res = []
        while cur:
            if cur.left:
                t = cur.left
                while t.right and t.right != cur:
                    t = t.right
                if t.right == cur:
                    t.right = None
                    cur = cur.right
                else:
                    res.append(cur.val)
                    t.right = cur
                    cur = cur.left
            else:
                res.append(cur.val)
                cur = cur.right
        return res

    #中序
    def LNR(self, root: TreeNode):
        cur = root
        res = []
        while cur:
            if cur.left:
                t = cur.left
                while t.right and t.right != cur:
                    t = t.right
                if t.right == cur:
                    res.append(cur.val)
                    t.right = None
                    cur = cur.right
                else:
                    t.right = cur
                    cur = cur.left
            else:
                res.append(cur.val)
                cur = cur.right
        return res

    #后序
    def LRN(self, root: TreeNode):
        res = []
        hair = TreeNode(0)
        hair.left = root
        cur = hair
        while cur:
            if cur.left:
                t = cur.left
                while t.right and t.right != cur:
                    t = t.right
                if t.right == cur:
                    x = cur.left
                    index = len(res)
                    while x != t:
                        res.insert(index,x.val)
                        x = x.right
                    res.insert(index, x.val)
                    t.right = None
                    cur = cur.right
                else:
                    t.right = cur
                    cur = cur.left
            else:
                cur = cur.right
        return res


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(10)
root.left.right = TreeNode(12)
root.right.left = TreeNode(8)
root.right.right = TreeNode(9)
t = MorrisTraversal()
print(t.NLR(root))
print(t.LNR(root))
print(t.LRN(root))

# 5 4 10 12 3 8 9
# 10 4 12 5 8 3 9
# 10 12 4 8 9 3 5

