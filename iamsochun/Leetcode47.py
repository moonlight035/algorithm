from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def done(t: List[int], temp: List[int]):
            if len(t) == 0:
                res.append(temp.copy())
            for i in range(len(t)):
                if i > 0 and t[i] == t[i-1]:
                    continue
                v = t.pop(i)
                temp.append(v)
                done(t,temp)
                temp.pop()
                t.insert(i,v)
        done(nums,[])
        return res

s = Solution()
print(s.permuteUnique([1,1,2]))