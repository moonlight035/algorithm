class Solution:
    def countSubstrings(self, s: str) -> int:
        t = '#' + '#'.join(s) + '#'
        dp = [1]*len(t)
        res = 0
        l = len(t)
        pos = 0
        bidge = 0
        for i in range(l):
            if i < bidge:
                dp[i] = min(bidge - i + 1, dp[pos*2 - i])
            while i+dp[i] < l and i - dp[i] >= 0 and t[i+dp[i]] == t[i-dp[i]]:
                dp[i] += 1
            res += dp[i] // 2
            if i + dp[i] - 1 > bidge:
                bidge = i + dp[i] - 1
                pos = i
        return res
