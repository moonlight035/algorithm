import math
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] == 0:
                left = mid
                break
            elif nums[mid] > 0:
                right = mid
            else:
                left = mid+1
        while left < len(nums) and nums[left] <= 0:
            left = left + 1
        i = 1
        while left < len(nums) and nums[left] == i:
            i = i+1
            left = left+1
            while left < len(nums) and nums[left]==nums[left-1]:
                left = left+1
        return i

    def other(self, nums: List[int]) -> int:
        a = [0]*10
        a[0] = 1
        for i in nums:
            if i > 0 and i <= len(nums):
                t = i//10
                l = i%10
                a[l] = a[l] | 1<<t
        r = a[0]
        for i in range(1,10):
            r = r & a[i]
        index = 0
        while bin(r)[-1] != '0':
            r = r>>1
            index = index + 1
        for i in range(10):
            m = bin(a[i]>>index)[-1]
            if m == '0':
                return index*10+i

    def another(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        for i in range(n):
            x = abs(nums[i])
            if x <= n and nums[x-1] > 0:
                nums[x-1] = -nums[x-1]
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1
    def ananother(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i]>=1 and nums[i] <= n and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1


# s = Solution()
# print(s.other(
#     [98,93,95,10,91,4,90,88,56,84,65,62,83,80,78,60,73,77,76,29,63,12,57,17,69,68,50,11,31,33,8,42,38,7,0,37,48,26,20,44,46,43,52,51,47,18,49,58,2,39,30,81,22,55,36,40,15,27,21,32,64,41,53,19,28,24,9,25,3,59,66,82,61,70,23,34,71,54,74,-1,1,45,14,79,5,35,13,72,75,85,87,6,16,86,67,89,94,92,96,97]))
s = 2
while True:
    s = math.pow(s,s)
    print(s)