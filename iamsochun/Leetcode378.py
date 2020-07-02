from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = len(matrix)
        t = [[0,0]]
        def put(element:List[int]):
            if element in t:
                return
            i = 0
            while i < len(t):
                if matrix[t[i][0]][t[i][1]] <= matrix[element[0]][element[1]]:
                    break
                i = i + 1
            t.insert(i,element)
        x = None
        while k>0:
            x = t.pop()
            if x[0] < l-1:
                put([x[0]+1,x[1]])
            if x[1] < l-1:
                put([x[0],x[1]+1])
            k = k-1
        return matrix[x[0]][x[1]]

    def other(self, matrix: List[List[int]], k: int) -> int:
        length = len(matrix)
        def check(mid:int):
            i = length - 1
            j = 0
            num = 0
            while i >= 0 and j < length:
                if matrix[i][j] <= mid:
                    num = num + i + 1
                    j = j+1
                else:
                    i = i-1
            return num>=k


        l = matrix[0][0]
        r = matrix[-1][-1]
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


s = Solution()
print(s.other([[1,3,5],[6,7,12],[11,14,14]],6))