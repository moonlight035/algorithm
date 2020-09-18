import sys
import time
from typing import List


class Solution:
    def minCut(self, s: str) -> int:
        dp = [[0]*len(s) for _ in  range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 0
        for l in range(2, len(s) + 1):
            for start in range(len(s) - l + 1):
                if s[start] == s[start + l - 1] and (start + 1 >= start + l - 2 or dp[start + 1][start + l - 2] ==0):
                    dp[start][start + l - 1] = 0
                else:
                    m = sys.maxsize
                    for i in range(start, start + l -1):
                        m = min(m, dp[start][i] + dp[i+1][start+l-1] + 1)
                    dp[start][start + l - 1] = m
        return dp[0][len(s) - 1]
    def partition(self, s: str) -> List[List[str]]:
        res = [[s[0]]]
        for i in range(1, len(s)):
            size = len(res)
            for j in range(size):
                if res[j][-1] == s[i]:
                    temp = res[j].copy()
                    temp[-1] += s[i]
                    res.append(temp)
                if len(res[j]) > 1 and res[j][-2] == s[i]:
                    temp = res[j].copy()
                    temp[-2] += temp[-1] + s[i]
                    temp.pop()
                    res.append(temp)
                res[j].append(s[i])
        return res
        # 表示回文串
        length = len(s)
        dp = [[False] * length for _ in range(length)]

        for i in range(length):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True

        result = []
        path = []

        def helper(index):
            if index == length:
                result.append(path[:])
                return
            for i in range(index, length):
                if dp[index][i]:
                    path.append(s[index:i + 1])
                    helper(i + 1)
                    path.pop()

        helper(0)
        return result

    def other(self, s: str) -> List[List[str]]:
        # 表示回文串
        length = len(s)
        dp = [[False] * length for _ in range(length)]

        for i in range(length):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True

        result = []
        path = []

        def helper(index):
            if index == length:
                result.append(path[:])
                return
            for i in range(index, length):
                if dp[index][i]:
                    path.append(s[index:i + 1])
                    helper(i + 1)
                    path.pop()

        helper(0)
        return result
s = Solution()
start = time.time()
s.other("aaaaaaaaaaaaaaaaaaaaaaa")
print(time.time() - start)
start = time.time()
s.partition("aaaaaaaaaaaaaaaaaaaaaaa")
print(time.time() - start)