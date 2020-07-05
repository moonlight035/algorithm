from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left.sort()
        right.sort()
        l = left[-1] if left else 0
        r = n-right[0] if right else 0
        return l if l > r else r
