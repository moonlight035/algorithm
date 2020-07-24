class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[1]*m for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[n-1][m-1]