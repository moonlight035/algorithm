from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left] < numbers[right]:
                return numbers[left]
            mid = (left + right) // 2
            if numbers[mid] > numbers[left] or numbers[mid] > numbers[right]:
                left = mid+1
            elif numbers[mid] < numbers[left]:
                right = mid
            else:
                left += 1
        return numbers[left]
[2,2,2,0,1]