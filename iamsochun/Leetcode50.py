class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        base = x
        p = abs(n)
        while p:
            if p&1:
                res *= base
            base *= base
            p = p>>1
        if n > 0:
            return res
        else:
            return 1/res


