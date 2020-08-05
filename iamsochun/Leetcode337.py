# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        cache = {}
        def done(node: TreeNode, flag: bool):
            if node is None:
                return 0
            if cache.get((node,flag)) is not None:
                return cache[(node,flag)]
            temp = done(node.left, True) + done(node.right, True)
            if flag:
                temp = max(node.val+done(node.left,False)+done(node.right,False),temp)
            cache[(node,flag)] = temp
            return temp
        return done(root,True)

    def other(self, root: TreeNode) -> int:
        def done(node: TreeNode):
            if node is None:
                return [0,0]
            l = done(node.left)
            r = done(node.right)
            return [node.val+l[1]+r[1],max(l[0],l[1])+max([r[0],r[1]])]
        res = done(root)
        return max(res[0],res[1])