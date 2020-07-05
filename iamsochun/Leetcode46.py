from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def handle(value: List[int], remain: List[int]):
            if not remain:
                res.append(value.copy())
            else:
                for i in range(len(remain)):
                    x = remain.pop(0)
                    value.append(x)
                    handle(value,remain)
                    value.pop()
                    remain.append(x)
        handle([],nums)
        return res

s = Solution()
print(s.permute([1,2,3]))