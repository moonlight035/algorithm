from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        t = {}
        for i in range(len(numbers)):
            x = t.get(numbers[i])
            if x is not None:
                return [x,i+1]
            else:
                t[target-numbers[i]] = i+1