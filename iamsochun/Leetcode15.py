class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            d = {}
            for j in range(i+1,len(nums)):
                if d.get(nums[j]) is not None:
                    x = d.pop(nums[j])
                    x.append(nums[j])
                    result.append(x)
                if not (j > i+1 and nums[j] == nums[j-1]):
                    key = -(nums[i]+nums[j])
                    if key >= 0:
                        d[key] = [nums[i],nums[j]]
        return result

    def otherThreeSum(self,nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0 or len(nums)-i<3:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left+1 <= right and nums[left+1] == nums[left]:
                        left = left+1
                    left = left + 1
                    while right-1 >= left and nums[right-1] == nums[right]:
                        right = right-1
                    right = right-1
                elif nums[i] + nums[left] + nums[right] <0:
                    left = left + 1
                elif nums[i] + nums[left] + nums[right] >0:
                    right = right - 1
        return result


s = Solution()
print(s.threeSum([-2,-1,-1,0,2]))
print(s.otherThreeSum([-2,-1,-1,0,2]))
