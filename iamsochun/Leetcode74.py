from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        lx = len(matrix)
        ly = len(matrix[0])
        left = 0
        right = lx*ly-1
        while left <= right:
            mid = left + (right-left)//2
            x = mid // ly
            y = mid - x*ly
            if target == matrix[x][y]:
                return True
            if target < matrix[x][y]:
                right = mid -1
            else:
                left = mid + 1
        return False