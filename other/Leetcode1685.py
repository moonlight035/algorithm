from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        res = -1
        next = [[0,len(nums)-1]]
        while next:
            left,right = next.pop()
            while left <= right:
                mid = left + (right-left) // 2
                if nums[mid] == mid:
                    res = mid
                    right = mid - 1
                    next.clear()
                elif nums[mid] < mid:
                    next.append([mid + 1, right])
                    right = nums[mid]
                else:
                    next.append([nums[mid], right])
                    right = mid - 1
        return res
s = Solution()
print(s.findMagicIndex([32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]))
