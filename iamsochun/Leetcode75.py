from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leftIn = left = 0
        rightIn = right = len(nums) - 1
        while left <= right:
            if nums[left] == 2 and nums[right] == 0:
                nums[left] = nums[right] = 1
                nums[leftIn] = 0
                nums[rightIn] = 2
                left += 1
                leftIn += 1
                right -= 1
                rightIn -= 1
            else:
                if nums[left] == 0:
                    nums[left] = 1
                    nums[leftIn] = 0
                    left += 1
                    leftIn += 1
                elif nums[left] == 1:
                    left += 1
                if nums[right] == 2:
                    nums[right] = 1
                    nums[rightIn] = 2
                    right -= 1
                    rightIn -= 1
                elif nums[right] == 1:
                    right -= 1
    def other(self, nums: List[int]) -> None:
        leftIn = 0
        rightIn = len(nums) - 1
        curr = 0
        while curr <= rightIn:
            if nums[curr] == 0:
                nums[curr] = 1
                nums[leftIn] = 0
                leftIn += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr],nums[rightIn] = nums[rightIn],nums[curr]
                rightIn -= 1
            else:
                curr += 1
s = Solution()
a= [2,0,2,1,1,0]
s.sortColors(a)
print(a)