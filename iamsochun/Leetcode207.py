from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depen = {}
        depenNum = {}
        for i in prerequisites:
            if depen.get(i[1]) is None:
                depen[i[1]] = []
            depen[i[1]].append(i[0])
            depenNum[i[0]] = depenNum.get(i[0],0)+1
            depenNum[i[1]] = depenNum.get(i[1],0)
        handle = []
        for i in depenNum.copy().keys():
            if depenNum[i] == 0:
                handle.append(i)
                depenNum.pop(i)
        while handle:
            x = handle.pop()
            for i in depen.get(x,[]):
                depenNum[i] -= 1
                if depenNum[i] == 0:
                    handle.append(i)
                    depenNum.pop(i)
        return len(depenNum)==0

s = Solution()
print(s.canFinish(2,[[1,0]]))