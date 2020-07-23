import sys
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        lx = len(grid)
        ly = len(grid[0])
        res = [-1]*(lx*ly)
        used = [False]*(lx*ly)
        next = [0]
        res[0] = grid[0][0]
        direction = [[0,1],[1,0]]
        while next:
            index = self.getNext(res,next)
            if index == lx*ly-1:
                return res[lx*ly-1]
            used[index] = True
            x = index // ly
            y = index - x*ly
            for i in direction:
                if x+i[0] < lx and x+i[0] >= 0 and y+i[1] < ly and y+i[1] >= 0:
                    nextX = x+i[0]
                    nextY = y+i[1]
                    nextIndex = ly*nextX+nextY
                    if not used[nextIndex] and (res[nextIndex] == -1 or res[index]+grid[nextX][nextY] < res[nextIndex]):
                        if res[nextIndex] == -1:next.append(nextIndex)
                        res[nextIndex] = res[index] + grid[nextX][nextY]
        return res[lx*ly-1]

    def getNext(self, distance: List[int], next: List[int]):
        index = -1
        for i in next:
            if index == -1 or distance[i] < distance[index]:
                index = i
        next.remove(index)
        return index

    def other(self, grid: List[List[int]]) -> int:
        lx = len(grid)
        ly = len(grid[0])
        res = grid.copy()
        for i in range(1,ly):
            res[0][i] += res[0][i-1]

        for i in range(1,lx):
            for j in range(ly):
                if i == 0 and j == 0:continue
                if j > 0:
                    res[i][j] += min(res[i-1][j],res[i][j-1])
                else:
                    res[i][j] += res[i-1][j]
        return res[lx-1][ly-1]


