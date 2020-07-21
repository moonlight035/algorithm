from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def done(left: int, right: int) -> List[TreeNode]:
            if left <= right:
                res = []
                for i in range(left,right+1):
                    leftList = done(left,i-1)
                    rightList = done(i+1,right)
                    for m in leftList:
                        for n in rightList:
                            head = TreeNode(i)
                            head.left = m
                            head.right = n
                            res.append(head)
                return res
            else:
                return [None]
        res = done(1,n)
        if res[0] is None:
            return []
        else:
            return res

s = Solution()
print(s.generateTrees(0))