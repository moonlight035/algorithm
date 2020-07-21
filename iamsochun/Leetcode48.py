import math
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(math.floor(l/2)):
            for j in range(i,l-i-1):
                temp = matrix[i][j]
                bi = l - j - 1
                bj = i
                while bi != i or bj != j:
                    matrix[bj][l - bi - 1] =  matrix[bi][bj]
                    bi,bj = l - bj - 1,bi
                matrix[bj][l - bi - 1] = temp
