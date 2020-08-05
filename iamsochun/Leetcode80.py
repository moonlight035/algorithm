from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        waitIn = 0
        flag = True
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1] or flag:
                flag = not (i > 0 and nums[i] == nums[i - 1])
                nums[waitIn] = nums[i]
                waitIn += 1
                count += 1
        return count

s = Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))