from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        def done(v: int, remain: List[int], res: List[int]):
            if not remain:
                return res
            for i in range(n):
                x = v&(1<<i)
                y = v - (1<<i) if x > 0 else v + (1<<i)
                if y in remain:
                    remain.remove(y)
                    res.append(y)
                    r = done(y, remain,res)
                    if r:
                        return r
                    remain.append(y)
                    res.pop()
            return None
        return done(0,list(range(1,1<<n)),[0])

    def other(self, n: int) -> List[int]:
        res = [0]
        head = 1
        for i in range(1,n+1):
            for j in res[::-1]:
                res.append(head + j)
            head = head<<1
        return res