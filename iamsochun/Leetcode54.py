from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        a = b = 0
        c = len(matrix)-1
        d = len(matrix[0])-1
        res = []
        while a <= c and b <= d:
            res.extend(matrix[a][b:d+1])
            for i in range(a+1,c):
                res.append(matrix[i][d])
            if c > a:
                res.extend(reversed(matrix[c][b:d+1]))
            if d > b:
                for i in range(c-1,a,-1):
                    res.append(matrix[i][b])
            a = a+1
            c = c-1
            b = b+1
            d = d-1
        return res

s = Solution()
print(s.spiralOrder([[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12]]))