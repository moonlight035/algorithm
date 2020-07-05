from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        d = 0
        now = 0
        next = 0
        for i in range(l):
            if i <= now:
                next = max(next, nums[i] + i)
            else:
                now = next
                next = nums[i]+i
                d = d+1
        return d

s = Solution()
print(s.jump([2,3,1,1,4]))