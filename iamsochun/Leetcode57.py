from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if not intervals:
            return [newInterval]
        for i in range(len(intervals)+1):
            if i == len(intervals) or intervals[i][0] > newInterval[1] :
                res.append(newInterval)
                i = i-1
                break
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0],intervals[i][0])
                newInterval[1] = max(newInterval[1],intervals[i][1])
                res.append(newInterval)
                break
        for j in range(i+1,len(intervals)):
            if res[-1][1] < intervals[j][0]:
                res.append(intervals[j])
            else:
                res[-1][1] = max(res[-1][1],intervals[j][1])
        return res

s = Solution()
print(s.insert([[1,3],[6,9]],[2,5]))