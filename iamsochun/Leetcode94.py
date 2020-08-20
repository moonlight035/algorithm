from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        s = [root]
        res = []
        while s:
            t = s[-1]
            if t.left:
                s.append(t.left)
                t.left = None
            else:
                res.append(t.val)
                s.pop()
                if t.right:
                    s.append(t.right)
        return res

    def other(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        cur = root
        while cur:
            if cur.left:
                x = t = cur.left
                while t.right and t.right != cur:
                    t = t.right
                if t.right == cur:
                    res.append(cur.val)
                    cur = cur.right
                else:
                    t.right = cur
                    cur = x
            else:
                res.append(cur.val)
                cur = cur.right
        return res