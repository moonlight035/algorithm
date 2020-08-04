from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        iIndex = []
        jIndex = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    iIndex.append(i)
                    jIndex.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in iIndex or j in jIndex:
                    matrix[i][j] = 0

    def other(self, matrix: List[List[int]]) -> None:
        lx = len(matrix)
        ly = len(matrix[0])
        flag = False
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i == 0:
                        flag = True
                    else:
                        matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,lx):
            for j in range(1,ly):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for i in range(1,lx):
                matrix[i][0] = 0
        if flag:
            for i in range(0,ly):
                matrix[0][i] = 0
s = Solution()
a = [[0,1,2,0],
     [3,4,5,2],
     [1,3,1,5]]
s.other(a)
print(a)