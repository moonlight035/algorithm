from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def done(index: int, temp: List[int]):
            if index == len(nums):
                res.append(temp.copy())
            else:
                done(index+1,temp)
                temp.append(nums[index])
                done(index+1,temp)
                temp.pop()
        done(0,[])
        return res