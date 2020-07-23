from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        left = {}
        right = {}
        for i in range(len(intervals)):
            q = intervals[i]
            left[q[0]] = left.get(q[0],0) + 1
            right[q[1]] = right.get(q[1],0) + 1
        x = sorted(list(left.keys())+list(right.keys()))
        sum = -1
        start = 0
        for i in range(len(x)):
            if i > 0 and x[i] == x[i-1]:
                continue
            if sum == -1:
                start = x[i]
                sum = left.get(x[i],0) - right.get(x[i],0)
            else:
                sum += left.get(x[i],0)
                sum -= right.get(x[i],0)
            if sum == 0:
                res.append([start,x[i]])
                sum = -1
        return res

    def other(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = []
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][-1],i[1])
        return res

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))

