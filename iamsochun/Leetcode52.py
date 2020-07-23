from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        def done(before: List[int], a:List[int], b: List[int], c: List[int]):
            if len(before) == n:
                return 1
            count = 0
            l = len(before)
            for i in range(n):
                if not (a[i]+b[i-l]+c[i+l]):
                    before.append(i)
                    a[i] += 1
                    b[i-l] += 1
                    c[i+l] += 1
                    count += done(before,a,b,c)
                    before.pop()
                    a[i] -= 1
                    b[i - l] -= 1
                    c[i + l] -= 1
            return count
        return done([],[0]*n,[0]*(2*n-1),[0]*(2*n-1))

    def bit(self, n: int) -> int:
        valid = (1 << n)-1
        def done(row: int, a: int, b: int, c: int):
            if row == n:
                return 1
            count = 0
            now = valid & ~(a|b|c)
            while now != 0:
                t = (-now)&now
                now = now^t
                count += done(row+1,a|t,(b|t)>>1,(c|t)<<1)
            return count
        return done(0,0,0,0)
s = Solution()
print(s.bit(4))