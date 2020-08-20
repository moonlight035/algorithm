from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def done(index: int, temp: List[int]):
            res.append(temp.copy())
            for i in range(index, len(nums)):
                if i == index or nums[i] != nums[i - 1]:
                    temp.append(nums[i])
                    done(i+1,temp)
                    temp.pop()
        done(0, [])
        return res