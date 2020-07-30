class Solution:
    def integerBreak(self, n: int) -> int:
        res = [0]*n
        res[0] = 1
        for i in range(1, n):
            for j in range(1, (i+1)//2+1):
                res[i] = max(res[i], max(res[j-1], j) * max(res[i-j], i-j+1))
        return res[n-1]

    def other(self, n: int) -> int:
        if n <= 3:
            return n-1
        ans = 1
        while n > 4:
            ans = ans * 3
            n = n-3
        return n*ans
s = Solution()
print(s.integerBreak(10))
