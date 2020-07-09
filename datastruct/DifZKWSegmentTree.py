import sys
from typing import List


class DifZKWSegmentTree:

    class Node:
        def __init__(self):
            self.min = sys.maxsize
            self.max = -sys.maxsize


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
        for i in range(self.base - 2, 0, -1):
            self.arr[i].min = min(self.arr[i << 1].min, self.arr[(i << 1) + 1].min)
            self.arr[i].max = max(self.arr[i << 1].max, self.arr[(i << 1) + 1].max)

            self.arr[i << 1].min -= self.arr[i].min
            self.arr[i << 1].max -= self.arr[i].max

            self.arr[(i << 1) + 1].min -= self.arr[i].min
            self.arr[(i << 1) + 1].max -= self.arr[i].max

    def update(self,i,v):
        self.arr[i + self.base].min += v
        self.arr[i + self.base].max += v
        i = (i + self.base) >> 1
        while i > 0:
            n = min(self.arr[i<<1].min, self.arr[(i<<1)+1].min)
            self.arr[i<<1].min -= n
            self.arr[(i<<1)+1].min -= n
            self.arr[i].min += n

            x = max(self.arr[i<<1].max, self.arr[(i<<1)+1].max)
            self.arr[i<<1].max -= x
            self.arr[(i<<1)+1].max -= x
            self.arr[i].max += x

            i = i>>1
    def updateRange(self,l,r,v):
        i = self.base+l-1
        j = self.base+r+1
        while i^j^1:
            if not (i&1):
                self.arr[i+1].min += v
                self.arr[i+1].max += v

            n = min(self.arr[i].min, self.arr[i+1].min)
            self.arr[i>>1<<1].min -= n
            self.arr[(i>>1<<1)+1].min -= n
            self.arr[i>>1].min += n

            x = max(self.arr[i].max, self.arr[i+1].max)
            self.arr[i>>1<<1].max -= x
            self.arr[(i>>1<<1)+1].max -= x
            self.arr[i>>1].max += x

            if j&1:
                self.arr[j-1].min += v
                self.arr[j-1].max += v

            n = min(self.arr[j].min, self.arr[j - 1].min)
            self.arr[j>>1<<1].min -= n
            self.arr[(j>>1<<1)+1].min -= n
            self.arr[j >> 1].min += n

            x = max(self.arr[j].max, self.arr[j - 1].max)
            self.arr[j>>1<<1].max -= x
            self.arr[(j>>1<<1)+1].max -= x
            self.arr[j >> 1].max += x

            i = i>>1
            j = j>>1
        i = i >> 1
        while i > 0:
            n = min(self.arr[i<<1].min, self.arr[(i<<1) + 1].min)
            self.arr[i<<1].min -= n
            self.arr[(i<<1)+1].min -= n
            self.arr[i].min += n

            x = max(self.arr[i<<1].max, self.arr[(i<<1) + 1].max)
            self.arr[i<<1].max -= x
            self.arr[(i<<1) + 1].max -= x
            self.arr[i].max += x

            i = i>>1

    def getRange(self,l,r):
        i = self.base+l-1
        j = self.base+r+1
        left = [sys.maxsize, -sys.maxsize]
        right = [sys.maxsize, -sys.maxsize]
        while i^j^1:
            left[0] += self.arr[i].min
            left[1] += self.arr[i].max
            if not (i & 1):
                left[0] = min(left[0], self.arr[i+1].min)
                left[1] = max(left[1], self.arr[i+1].max)

            right[0] += self.arr[j].min
            right[1] += self.arr[j].max
            if j & 1:
                right[0] = min(right[0], self.arr[j - 1].min)
                right[1] = max(right[1], self.arr[j - 1].max)
            i = i>>1
            j = j>>1
        res = [min(left[0]+self.arr[i].min, right[0]+self.arr[j].min)
            , max(left[1]+self.arr[i].max, right[1]+self.arr[j].max)]
        i = i >> 1
        while i > 0:
            res[0] += self.arr[i].min
            res[1] += self.arr[i].max
            i = i>>1
        return res

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    t = DifZKWSegmentTree(a)
    for i in range(len(a)):
        print(t.getRange(0,i))
    print('```````````````````````````````````')
    for i in range(len(a)):
        print(t.getRange(i,len(a)-1))
    t.updateRange(0,3,8)
    print('````````````````````````````````````')
    for i in range(len(a)):
        print(t.getRange(0,i))
    print('`````````````````````````````````````````')
    t.update(6,8)
    for i in range(len(a)):
        print(t.getRange(0,i))
