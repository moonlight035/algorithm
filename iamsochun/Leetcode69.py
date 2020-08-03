class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left < right:
            mid = left + (right- left + 1)//2
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                left = mid
            else:
                right = mid -1
        return left

    #牛顿二分法
    def other(self, x: int) -> int:
        base = x
        while base > 0:
            next = 0.5*(base+x/base)
            if base - next <= 10**-5:
                break
            base = next
        return int(base)


