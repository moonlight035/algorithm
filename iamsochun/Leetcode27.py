from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = -1
        for j in range(len(nums)):
            if nums[j] != val:
                i = i+1
                nums[i] = nums[j]
        return i+1
