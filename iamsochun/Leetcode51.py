from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def done(before: List[int], a:List[int], b: List[int], c: List[int]):
            if len(before) == n:
                r = []
                for i in before:
                    r.append('.'*i+'Q'+'.'*(n-i-1))
                res.append(r)
                return
            l = len(before)
            for i in range(n):
                if not (a[i]+b[i-l]+c[i+l]):
                    before.append(i)
                    a[i] += 1
                    b[i-l] += 1
                    c[i+l] += 1
                    done(before,a,b,c)
                    before.pop()
                    a[i] -= 1
                    b[i - l] -= 1
                    c[i + l] -= 1
        done([],[0]*n,[0]*(2*n-1),[0]*(2*n-1))
        return res

s = Solution()
r = s.solveNQueens(4)
for i in r:
    for j in i:
        print(j)
    print('````````````````````````````')