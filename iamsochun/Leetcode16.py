import sys


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        best = sys.maxsize
        for i in range(len(nums)):
            if len(nums)-i<3:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            delta = nums[i] + nums[i + 1] + nums[i + 2] - target
            if delta > 0:
                if abs(delta) < abs(best-target):
                    best = delta + target
                break
            delta = nums[i] + nums[len(nums) - 2] + nums[len(nums) - 1] - target
            if delta < 0:
                if abs(delta) < abs(best-target):
                    best = delta + target
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == target:
                    return target
                else:
                    if abs(best-target) > abs(nums[i] + nums[left] + nums[right]-target):
                        best = nums[i] + nums[left] + nums[right]
                    if nums[i] + nums[left] + nums[right] < target:
                        left = left + 1
                    else:
                        right = right - 1
        return best
s = Solution()
print(s.threeSumClosest([-1,2,1,-4],1))