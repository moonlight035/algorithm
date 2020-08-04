class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        res = [[0]*(l2+1) for _ in range(l1+1)]
        for i in range(l2+1):
            res[0][i] = i
        for i in range(l1+1):
            res[i][0] = i
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                res[i][j] = min(res[i-1][j] + 1, res[i][j-1] + 1
                                , res[i-1][j-1] if word1[i-1] == word2[j-1] else res[i-1][j-1]+1)
        return res[l1][l2]
