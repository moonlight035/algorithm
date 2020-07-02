from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if not nums or nums[mid] != target:
            return [-1, -1]
        x = mid
        while left < x:
            t = (left + x) // 2
            if nums[t] == target:
                # if t-1>=left and nums[t-1] != target:
                #     left = t
                #     break
                x = t
            else:
                left = t+1
        x = mid
        while right > x:
            t = (right + x +1) // 2
            if nums[t] == target:
                # if t + 1 <= right and nums[t + 1] != target:
                #     right = t
                #     break
                x = t
            else:
                right = t - 1
        return [left,right]

s = Solution()
print(s.searchRange([5,7,7,8,8,10],8))