from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        ans = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack[-1] >= 0 and heights[stack[-1]] > heights[i]:
                x = stack.pop()
                start = stack[-1] + 1
                ans = max(ans , heights[x]*(i-start))
            stack.append(i)
        return ans

s = Solution()
print(s.largestRectangleArea([2,1,2]))