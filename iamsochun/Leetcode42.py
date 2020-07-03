from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0
        next = [0]*n
        next[n-1] = n-1
        for i in range(n-2,-1,-1):
            if height[i] > height[next[i+1]]:
                next[i] = i
            else:
                next[i] = next[i+1]
        left = 0
        while left < n-2:
            if height[left+1] >= height[left]:
                left = left+1
                continue
            behind = next[left+1]
            if height[behind] > height[left]:
                right = left+1
                while height[right] < height[left]:
                    right = right+1
                res += (right-left-1)*height[left]-sum(height[left+1:right])
                left = right
            elif height[behind] <= height[left]:
                if behind == left+1:
                    left = behind
                    continue
                res += (behind-left-1)*height[behind]-sum(height[left+1:behind])
                left = behind
        return res

    def other(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        res = 0
        while left <= right:
            if leftMax <= rightMax:
                if height[left]<leftMax:
                    res += min(leftMax,rightMax)-height[left]
                else:
                    leftMax = height[left]
                left = left+1
            else:
                if height[right]<rightMax:
                    res += min(leftMax, rightMax) - height[right]
                else:
                    rightMax = height[right]
                right = right-1
        return res

s = Solution()
print(s.other([0,1,0,2,1,0,1,3,2,1,2,1]))
