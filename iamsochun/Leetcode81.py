from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[right]:
                right -= 1
            elif target > nums[mid]:
                if nums[mid] > nums[right] or nums[mid] < nums[right] and target <= nums[right]:
                    left = mid + 1
                if nums[mid] < nums[right] and target > nums[right]:
                    right = mid - 1
            elif target < nums[mid]:
                if nums[mid] < nums[right] or nums[mid] > nums[right] and target >= nums[left]:
                    right = mid -1
                if nums[mid] > nums[right] and target < nums[left]:
                    left = mid + 1
        return False
