from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        sum = nums[0]
        for i in nums[1:]:
            if sum < 0:
                sum = i
            else:
                sum = sum+i
            if sum > max:
                max = sum
        return max

    def other(self, nums: List[int]) -> int:
        def done(left: int, right: int):
            if left == right:
                return [nums[left],nums[left],nums[left],nums[left]]
            mid = left + (right-left)//2
            [a,b,c,n] = done(left,mid)
            [d,e,f,m] = done(mid+1,right)
            x = max(b,e,(c+d))
            l = n+d if n+d > a else a
            r = m+c if m+c > f else f
            return [l,x,r,n+m]
        return done(0,len(nums)-1)[1]

s = Solution()
print(s.other([1,2,-1,-2,2,1,-2,1,4,-5,4]))

#4-8