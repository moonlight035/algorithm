# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        before = left = leftNext = right = None
        cur = root
        while cur:
            if cur.left:
                t = cur.left
                while t.right and t.right != cur:
                    t = t.right
                if t.right == cur:
                    t.right = None
                    if before and before.val > cur.val:
                        if not left:
                            left = before
                            leftNext = cur
                        else:
                            right = cur
                    before = cur
                    cur = cur.right
                else:
                    t.right = cur
                    cur = cur.left
            else:
                if before and before.val > cur.val:
                    if not left:
                        left = before
                        leftNext = cur
                    else:
                        right = cur
                before = cur
                cur = cur.right
        if not right:
            left.val, leftNext.val = leftNext.val, left.val
        else:
            left.val, right.val = right.val, left.val


s = Solution()