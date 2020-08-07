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

    def other(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        lx = len(matrix)
        ly = len(matrix[0])
        left = [0]*ly
        right = [ly-1]*ly
        height = [0]*ly
        ans = 0
        for i in range(lx):
            curLeft,curRight = 0,ly-1
            for j in range(ly):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(ly):
                if matrix[i][j] == '1':
                    left[j] = max(curLeft,left[j])
                else:
                    left[j] = 0
                    curLeft = j+1
            for j in range(ly-1,-1,-1):
                if matrix[i][j] == '1':
                    right[j] = min(curRight,right[j])
                else:
                    right[j] = ly-1
                    curRight = j-1
            for j in range(ly):
                ans = max(ans, (right[j] - left[j] + 1)*height[j])
        return ans

s = Solution()
print(s.other([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]))
