from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        number = 1
        for start in range((n+1)//2):
            for i in range(start,n-start):
                res[start][i] = number
                number += 1
            for i in range(start+1, n-start):
                res[i][n-start-1] = number
                number += 1

            for i in range(n-start-2,start-1,-1):
                res[n-start-1][i] = number
                number += 1
            for i in range(n-start-2,start,-1):
                res[i][start] = number
                number += 1
        return res



