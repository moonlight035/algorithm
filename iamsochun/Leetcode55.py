from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        now = 0
        for i in range(len(nums)):
            if i <= now:
                now = max(now,nums[i]+i)
                if now >= len(nums)-1:
                    return True
            else:
                return False
s = Solution()
print(s.canJump(
[1,2,3]))