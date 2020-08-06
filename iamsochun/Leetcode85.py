from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        temp = [0]*len(matrix[0])
        res = 0
        for i in range(len(matrix)):
            self.add(temp,matrix[i])
            res = max(res, self.largestRectangleArea(temp.copy()))
        return res

    def add(self,temp: List[int], next: List[str]):
        for i in range(len(temp)):
            if next[i] == '0':
                temp[i] = 0
            else:
                temp[i] += 1

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
print(s.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]))
