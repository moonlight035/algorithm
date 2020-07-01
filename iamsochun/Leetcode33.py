from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(left,right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target: return mid
                elif nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            return -1

        def done(left,right):
            if left>right:
                return -1
            mid = (left+right)//2
            if nums[mid] == target:return mid
            if target > nums[mid]:
                if nums[right] < nums[mid]:
                    return done(mid+1,right)
                elif target <= nums[right]:
                    return binarySearch(mid+1,right)
                else:
                    return done(left,mid-1)
            else:
                if nums[left] > nums[mid]:
                    return done(left,mid-1)
                elif target >= nums[left]:
                    return binarySearch(left,mid-1)
                else:
                    return done(mid+1,right)
        if not nums:
            return -1
        return done(0,len(nums)-1)

    def other(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:return mid
            if mid+1<len(nums) and nums[right] >= nums[mid+1]:
                if target >= nums[mid+1] and target <= nums[right]:
                    left = mid +1
                else:
                    right = mid -1
            else:
                if target >= nums[left] and target <= nums[mid-1]:
                    right = mid-1
                else:
                    left = mid+1
        return -1


s = Solution()
print(s.other([4,5,6,7,0,1,2],5))