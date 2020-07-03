from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def handle(index: int, target: int, before: List[int], flag: bool):
            if target == 0:
                res.append(before.copy())
                return
            elif index == len(candidates) or candidates[index] > target:
                return
            handle(index+1,target,before,False)
            if index == 0 or candidates[index] != candidates[index-1] or flag:
                before.append(candidates[index])
                handle(index+1,target-candidates[index],before,True)
                before.remove(candidates[index])
        candidates.sort()
        handle(0,target,[])
        return res
    def other(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrace(i, summ, comb):
            nonlocal res
            if summ > target:
                return
            if summ == target:
                # if comb not in res:
                res.append(comb)
                return

            for j in range(i, n):
                if summ + candidates[j] > target:
                    break
                if j > i and candidates[j - 1] == candidates[j]:
                    # print(j,candidates[j])
                    continue
                backtrace(j + 1, summ + candidates[j], comb + [candidates[j]])

        backtrace(0, 0, [])
        return res

s = Solution()
print(s.other([1,1,1,1],3))