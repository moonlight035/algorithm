class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0]*(len(s) + 1)
        dp[0] = dp[1] = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] in ['1','2']:
                    dp[i + 1] = dp[i - 1]
                else:
                    return 0
            elif s[i - 1] == '0' or int(s[i - 1:i+1]) > 26:
                dp[i + 1] = dp[i]
            else:
                dp[i + 1] = dp[i]+dp[i - 1]
        return dp[len(s)]
