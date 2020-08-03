import sys
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        l = len(nums)
        index = [0]*l
        tree = ZKWSegmentTree([0]*l)
        for i in range(l):
            tree.update(i,nums[i][0])
        min = tree.getRange()
        while True:
            next = tree.getMinIndex()
            if len(nums[next])-1 == index[next]:
                break
            index[next] += 1
            tree.update(next,nums[next][index[next]]-nums[next][index[next]-1])
            temp = tree.getRange()
            if temp[1] - temp[0] < min[1] - min[0]:
                min = temp
        return min

    def other(self, nums: List[List[int]]) -> List[int]:
        l = len(nums)
        cache = {}
        minValue = 10**5
        maxValue = -10**5
        for i in range(l):
            minValue = min(minValue, nums[i][0])
            maxValue = max(maxValue, nums[i][-1])
            for j in range(len(nums[i])):
                if cache.get(nums[i][j]) is None:
                    cache[nums[i][j]] = [i]
                else:
                    cache[nums[i][j]].append(i)
        left = right = minValue
        count = 0
        appear = [0]*l
        res = [minValue, maxValue]
        while right <= maxValue:
            for i in cache.get(right,[]):
                appear[i] += 1
                if appear[i] == 1:
                    count += 1
            while count == len(nums) and left <= right:
                if right - left < res[1] - res[0]:
                    res[1],res[0] = right,left
                for i in cache.get(left,[]):
                    appear[i] -= 1
                    if appear[i] == 0:
                        count -= 1
                left += 1
            right += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.other([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))


class ZKWSegmentTree:

    class Node:
        def __init__(self):
            self.min = sys.maxsize
            self.max = -sys.maxsize
            self.index = 0

    def __init__(self, arr: List[int]):
        n = len(arr)
        i = 1
        while i < n+1:
            i = i<<1
        self.n = n
        self.base = i+1
        self.arr = [self.Node() for _ in range(i*2)]
        for i in range(self.n):
            self.arr[self.base+i].min = self.arr[self.base+i].max = arr[i]
            self.arr[self.base+i].index = i

        for i in range(self.base - 2, 0, -1):
            if self.arr[i<<1].min <= self.arr[(i<<1)+1].min:
                self.arr[i].min = self.arr[i<<1].min
                self.arr[i].index = self.arr[i << 1].index
            else:
                self.arr[i].min = self.arr[(i<<1)+1].min
                self.arr[i].index = self.arr[(i << 1) + 1].index
            self.arr[i].max = max(self.arr[i<<1].max,self.arr[(i<<1)+1].max)


    def update(self,i,v):

        self.arr[i + self.base].min += v
        self.arr[i + self.base].max += v
        i = (i + self.base) >> 1
        num = 2
        while i > 0:
            left = self.arr[i << 1]
            right = self.arr[(i << 1) + 1]
            now = self.arr[i]
            if left.min <= right.min:
                now.min = left.min
                now.index = left.index
            else:
                now.min = right.min
                now.index = right.index
            now.max = max(left.max, right.max)
            i = i >> 1
            num = num << 1

    def getRange(self):
        return [self.arr[1].min, self.arr[1].max]

    def getMinIndex(self):
        return self.arr[1].index