import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def done(node: TreeNode):
            if not node:
                return [sys.maxsize, -sys.maxsize, True]
            [ml,xl,sl] = done(node.left)
            [mr,xr,sr] = done(node.right)
            if sl and sr and xl < node.val < mr:
                return [min(ml,node.val),max(xr,node.val),True]
            else:
                return [ml,xr,False]
        return done(root)[2]

    def other(self, root: TreeNode) -> bool:
        cur = root
        before = -sys.maxsize
        while cur:
            if cur.left:
                m = cur.left
                while m.right and m.right != cur:
                    m = m.right
                if m.right == cur:
                    m.right = None
                    if cur.val <= before:return False
                    before = cur.val
                    cur = cur.right
                else:
                    m.right = cur
                    cur = cur.left
            else:
                if cur.val <= before: return False
                before = cur.val
                cur = cur.right
        return True

