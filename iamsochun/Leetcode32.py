# I am SB
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [[0 for _ in s]  for _ in s]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                dp[i][i] = 1
            else:
                dp[i][i] = 0
        i = 0
        while i < len(s):
            if dp[i][i] == 0:
                i = i+1
                continue
            for j in range(i+1,len(s)):
                if s[j] == '(':
                    dp[i][j] = dp[i][j-1]+1
                else:
                    if dp[i][j-1]>0:
                        dp[i][j] = dp[i][j-1] - 1
                    else:
                        i = j+1
                        break
                if dp[i][j] == 0 and j-i+1 > res:
                    res = j-i+1
            if j==len(s):break
        return res

    def other(self, s: str) -> int:
        i = 0
        res = 0
        while i < len(s):
            if s[i] == '(':
                right = 1
            else:
                i = i+1
                continue
            num = 0
            flag = True
            for j in range(i+1,len(s)):
                if s[j] == '(':
                    right = right+1
                else:
                    if right>0:
                        right = right - 1
                        num = num+1
                    else:
                        i = j+1
                        flag = False
                        break
                if right == 0 and j-i+1 > res:
                    num = 0
                    res = j-i+1
            if flag:
                res = max(res,2*num)
                break
        return res
s = Solution()
print(s.other("(()(((()"))