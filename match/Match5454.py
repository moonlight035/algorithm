from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        lx = len(mat)
        ly = len(mat[0])
        sum = 0
        for i in range(lx):
            r = [1]*ly
            for j in range(i,lx):
                r = [m and n for m,n in zip(r,mat[j])]
                t = 0
                k = 0
                while k <= ly:
                    if k < ly and r[k] == 1:
                        t = t+1
                    else:
                        sum += (t+1)*t/2
                        t = 0
                    k = k+1
        return int(sum)

s = Solution()
print(s.numSubmat([[1,0,1],[1,1,0],[1,1,0]]))
