from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def done(start: int, num: int, temp: List[int]):
            if num == 0:
                res.append(temp.copy())
                return
            for i in range(start, n - num + 2):
                temp.append(i)
                done(i+1,num-1,temp)
                temp.pop()
        done(1,k,[])
        return res
    def other(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = [0 for i in range(k+1)]
        i = 0
        while i >= 0:
            temp[i] += 1
            if temp[i] > n-k+i+1:
                i -= 1
            elif i == k-1:
                res.append(temp.copy())
            else:
                temp[i+1] = temp[i]
                i =i+1
        return res


s = Solution()
print(s.combine(4,2))