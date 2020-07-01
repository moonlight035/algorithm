# I am SB
class Solution:

    #动态规划  dp[i]代表以i结尾的最长有效括号
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = [0]*len(s)
        for i in range(1,len(s)):
            if s[i] == ')':
                pre = i-dp[i-1]-1
                if pre >= 0 and s[pre] == '(':
                    dp[i] = dp[i-1]+2
                    if pre>=2:
                        dp[i] = dp[i] + dp[pre-1]
        return max(dp)


    def other(self, s: str) -> int:
        res = 0
        start = 0
        more = 0
        for i in range(len(s)):
            if s[i] == '(':
                more = more+1
            elif more >0:
                more = more-1
            else:
                more = 0
                start = i+1
            if more == 0 and i-start+1>res:
                res = i-start+1
        start = len(s)-1
        more = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ')':
                more = more+1
            elif more >0:
                more = more-1
            else:
                more = 0
                start = i-1
            if more == 0 and start-i+1 > res:
                res = start-i+1
        return res

    def another(self, s: str) -> int:
        t = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                t.append(i)
            else:
                t.pop()
                if not t:
                    t.append(i)
                else:
                    x = i-t[len(t)-1]
                    if x > res:
                        res = x
        return res

s = Solution()
print(s.other("(()))())("))