from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def handle(index: int, target: int, before: List[int]):
            if target == 0:
                res.append(before.copy())
                return
            # 结束 和 剪枝
            elif index == len(candidates) or candidates[index] > target:
                return
            # 当前index不取
            handle(index+1,target,before)
            # 递归当前index所有能取得数量
            i = 1
            while i*candidates[index] <= target:
                before.append(candidates[index])
                handle(index+1,target-i*candidates[index],before)
                i = i+1
            # 回溯
            for j in range(i-1):
                before.remove(candidates[index])
        candidates.sort()
        handle(0,target,[])
        return res
s = Solution()
print(s.combinationSum([2,3,6,7],7))

