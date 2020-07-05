from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        ls = len(s)
        lp = len(p)
        dp = [[False] * (lp + 1) for _ in range(ls + 1)]
        dp[0][0] = True
        for i in range(1, lp + 1):
            dp[0][i] = dp[0][i - 1] and p[i - 1] == '*'
        quick = dp[0].copy()
        for i in range(1, ls + 1):
            for j in range(1, lp + 1):
                if p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = quick[j] or dp[i][j-1]
                else:
                    dp[i][j] = s[i - 1] == p[j - 1] and dp[i - 1][j - 1]
                quick[j] = quick[j] or dp[i][j]
        return dp[ls][lp]

    def other(self, s: str, p: str) -> bool:
        if not p:
            return not s
        ls = len(s)
        lp = len(p)

        i = 0
        j = 0
        c = -1
        next = -1
        while i < ls:
            if j < lp and (p[j] == '?' or p[j] == s[i]):
                i = i+1
                j = j+1
            elif j < lp and (p[j] == '*'):
                while i < ls and j < lp and s[i] != p[j]:
                    if p[j] == '?':
                        i = i+1
                        j = j+1
                    elif p[j] == '*':
                        j = j+1
                    else:
                        i = i+1
                if j == lp: return True
                next = i+1
                c = j
            elif c > -1:
                    i = next
                    while i < ls and s[i] != p[c]:
                        i = i + 1
                    next = i + 1
                    j = c
            else:
                return False
        while j < lp and p[j] == '*':
            j = j+1
        return j==lp


s = Solution()
print(s.other("zacabz","*a?b*"))
