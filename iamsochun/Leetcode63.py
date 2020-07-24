from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        lx = len(obstacleGrid)
        ly = len(obstacleGrid[0])
        res = [[0]*ly for _ in range(lx)]
        if obstacleGrid[lx-1][ly-1]:
            return 0
        else:
            res[lx-1][ly-1] = 1

        for i in range(lx-2,-1,-1):
            if obstacleGrid[i][ly-1] == 0:
                res[i][ly-1] = 1
            else:break

        for i in range(ly-2,-1,-1):
            if obstacleGrid[lx-1][i] == 0:
                res[lx-1][i] = 1
            else:break


        for i in range(lx-2,-1,-1):
            for j in range(ly-2,-1,-1):
                if obstacleGrid[i][j] == 0:
                    res[i][j] = res[i+1][j] + res[i][j+1]
                else:
                    res[i][j] = 0
        return res[0][0]
