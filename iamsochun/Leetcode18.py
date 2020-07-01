import sys


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        best = sys.maxsize
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = len(nums)-1
                while left<right:
                    x = nums[i]+nums[j]+nums[left]+nums[right]
                    if x==target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left = left+1
                        while left<=right and nums[left] == nums[left-1]:
                            left = left+1
                        right = right - 1
                        while right>=left and nums[right] == nums[right+1]:
                            right = right-1
                    elif x > target:
                        right = right-1
                    else:
                        left = left+1
        return res

s = Solution()
print(s.fourSum([0,0,0,0], 1))
