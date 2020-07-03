# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def tree(left: int, right: int):
            if left > right:
                return None
            if left == right:
                return TreeNode(nums[left])
            mid = (left + right)//2
            t = TreeNode(nums[mid])
            t.left = tree(left,mid-1)
            t.right = tree(mid+1,right)
            return t
        return tree(0,len(nums)-1)

