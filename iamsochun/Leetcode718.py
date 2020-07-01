import math
from typing import List

# 将问题转换为寻找所有A、B子数组组合尾部对齐后的最长后缀
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    res = max(dp[i+1][j+1],res)
        return res

    def other(self, A: List[int], B: List[int]) -> int:
        def maxLength(addA: int, addB: int, length: int) -> int:
            ret = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        n, m = len(A), len(B)
        ret = 0
        for i in range(n):
            length = min(m, n - i)
            ret = max(ret, maxLength(i, 0, length))
        for i in range(m):
            length = min(n, m - i)
            ret = max(ret, maxLength(0, i, length))
        return ret



    def another(self, A: List[int], B: List[int]) -> int:
        base, mod = 113, 10 ** 9 + 9
        def check(length: int) -> bool:
            hashA = 0
            for i in range(length):
                hashA = (hashA * base + A[i]) % mod
            bucketA = {hashA}
            mult = pow(base, length - 1, mod)
            for i in range(length, len(A)):
                hashA = ((hashA - A[i - length] * mult) * base + A[i]) % mod
                bucketA.add(hashA)

            hashB = 0
            for i in range(length):
                hashB = (hashB * base + B[i]) % mod
            if hashB in bucketA:
                return True
            for i in range(length, len(B)):
                hashB = ((hashB - B[i - length] * mult) * base + B[i]) % mod
                if hashB in bucketA:
                    return True

            return False

        left, right = 0, min(len(A), len(B))
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


s = Solution()
print(s.another([0,0,0,0,0],[0,0,0,0,0]))