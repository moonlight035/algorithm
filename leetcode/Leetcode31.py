from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = l-2
        while i >=0:
            if nums[i] < nums[i+1]:
                for j in range(i+1,(l+i)//2+1):
                        b = nums[j]
                        nums[j] = nums[l+i-j]
                        nums[l+i-j] = b
                for j in range(i+1,l):
                    if nums[j] > nums[i]:
                        b = nums[j]
                        nums[j] = nums[i]
                        nums[i] = b
                        break
                break
            i = i-1
        if i < 0:
            for j in range(0, (l - 1) // 2+1):
                b = nums[j]
                nums[j] = nums[l + i - j]
                nums[l + i - j] = b

s = Solution()
a = [1,3,2]
s.nextPermutation(a)
print(a)
