import math
import sys


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min_int = -math.pow(2,31)
        max_int = math.pow(2,31) - 1
        if dividend == min_int and divisor == -1:
            return int(max_int)
        def div(x: int, y: int) -> int:
            if x > y:return 0
            count = 1
            a = x
            b = y
            while a <= (b+b):
                count = count + count
                b = b + b
            return count + div(x-count*y,y)
        dividendTemp = -dividend if dividend>0 else dividend
        divisorTemp = -divisor if divisor>0 else divisor
        count = div(dividendTemp,divisorTemp)
        if dividend<0 and divisor<0 or dividend>0 and divisor>0:
            return count
        else:
            return -count

s = Solution()
print(s.divide(-2147483648,-1))
