class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False]*(len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j-1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = s1[i - 1] == s3[i + j - 1] and dp[i - 1][j] or s2[j - 1] == s3[i + j -1] and dp[i][j - 1]
        return dp[len(s1)][len(s2)]

    def other(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        i = j = k = 0
        s = []
        repeat = {}
        while i < len(s1) or j < len(s2):
            if i < len(s1) and s1[i] == s3[k] and j < len(s2) and s2[j] == s3[k]:
                if repeat.get((i, j+1, k+1), True):
                    s.append([i,j+1,k+1])
                    repeat[(i, j+1, k+1)] = False
                i += 1
                k += 1
            elif i < len(s1) and s1[i] == s3[k]:
                i += 1
                k += 1
            elif j < len(s2) and s2[j] == s3[k]:
                j += 1
                k += 1
            elif s:
                i, j, k = s.pop()
            else:
                return False
        return i == len(s1) and j == len(s2) and k == len(s3)

    def another(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        repeat = {}
        s = [(0,0)]
        while s:
            i, j = s.pop()
            k = i + j
            if i == len(s1) and j == len(s2):
                return True
            if i < len(s1) and s1[i] == s3[k]  and repeat.get((i+1, j), True):
                s.append((i+1, j))
                repeat[(i+1, j)] = False
            if j < len(s2) and s2[j] == s3[k] and repeat.get((i, j+1), True):
                s.append((i, j+1))
                repeat[(i, j+1)] = False
        return False


s = Solution()
print(s.other("bcc",
"bbca",
"bbcbcac"))
#  bac         bed             bacedb
#
# 77  70  69
# dp[][] dp[0][0]  dp[i][j] = dp[i-1][j]
# 1  ---- i
# 1 - --- j
# 1 ---- i+j
# if s3[i+j] == s1[i]  dp[i-1][j]
# if s3[i+j] == s2[j] dp[i][j-1]
#
#
