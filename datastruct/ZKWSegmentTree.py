import sys
from typing import List


class ZKWSegmentTree:

    class Node:
        def __init__(self):
            self.min = sys.maxsize
            self.max = -sys.maxsize
            self.sum = 0
            self.add = 0

    def __init__(self, arr: List[int]):
        n = len(arr)
        i = 1
        while i < n+1:
            i = i<<1
        self.n = n
        self.base = i+1
        self.arr = [self.Node() for _ in range(i*2)]
        for i in range(self.n):
            self.arr[self.base+i].min = self.arr[self.base+i].max = self.arr[self.base+i].sum = arr[i]

        for i in range(self.base - 2, 0, -1):
            self.arr[i].min = min(self.arr[i<<1].min,self.arr[(i<<1)+1].min)
            self.arr[i].max = max(self.arr[i<<1].max,self.arr[(i<<1)+1].max)
            self.arr[i].sum = self.arr[i<<1].sum + self.arr[(i<<1)+1].sum

    def update(self,i,v):
        self.arr[i + self.base].sum += v
        self.arr[i + self.base].min += v
        self.arr[i + self.base].max += v
        i = (i + self.base) >> 1
        num = 2
        while i > 0:
            left = self.arr[i << 1]
            right = self.arr[(i << 1) + 1]
            now = self.arr[i]
            now.min = min(left.min, right.min) + now.add
            now.max = max(left.max, right.max) + now.add
            now.sum = left.sum + right.sum + now.add * num
            i = i >> 1
            num = num << 1

    def updateRange(self,l,r,v):
        lnum, rnum, num = 0, 0, 1
        i = self.base+l-1
        j = self.base+r+1
        while i^j^1:
            if not (i&1):
                self.arr[i+1].min += v
                self.arr[i+1].max += v
                self.arr[i+1].sum += num*v
                self.arr[i+1].add += v
                lnum += num
            self.arr[i >> 1].min = min(self.arr[i >> 1 << 1].min, self.arr[(i >> 1 << 1) + 1].min) + self.arr[i >> 1].add
            self.arr[i >> 1].max = max(self.arr[i >> 1 << 1].max, self.arr[(i >> 1 << 1) + 1].max) + self.arr[i >> 1].add
            self.arr[i >> 1].sum = self.arr[i >> 1 << 1].sum + self.arr[(i >> 1 << 1) + 1].sum + self.arr[i >> 1].add * lnum

            if j&1:
                self.arr[j-1].min += v
                self.arr[j-1].max += v
                self.arr[j-1].sum += num*v
                self.arr[j-1].add += v
                rnum += num
            self.arr[j >> 1].min = min(self.arr[j >> 1 << 1].min, self.arr[(j >> 1 << 1) + 1].min) + self.arr[j >> 1].add
            self.arr[j >> 1].max = max(self.arr[j >> 1 << 1].max, self.arr[(j >> 1 << 1) + 1].max) + self.arr[j >> 1].add
            self.arr[j >> 1].sum = self.arr[j >> 1 << 1].sum + self.arr[(j >> 1 << 1) + 1].sum + self.arr[j >> 1].add*lnum
            i = i >> 1
            j = j >> 1
            num = num << 1
        i = i >> 1
        while i > 0:
            self.arr[i].min = min(self.arr[i<<1].min, self.arr[(i<<1)+1].min)+self.arr[i].add
            self.arr[i].max = max(self.arr[i << 1].max, self.arr[(i << 1) + 1].max) + self.arr[i].add
            self.arr[i].sum = self.arr[i << 1].sum + self.arr[(i << 1) + 1].sum + self.arr[i].add*(lnum+rnum)
            i = i >> 1

    def getRange(self,l,r):
        lnum,rnum,num = 0,0,1
        left,right = [sys.maxsize,-sys.maxsize,0],[sys.maxsize,-sys.maxsize,0]
        i = self.base+l-1
        j = self.base+r+1
        while i^j^1:
            if lnum:
                left[0] += self.arr[i].add
                left[1] += self.arr[i].add
                left[2] += self.arr[i].add*lnum
            if rnum:
                right[0] += self.arr[j].add
                right[1] += self.arr[j].add
                right[2] += self.arr[j].add*rnum
            if not (i&1):
                left[0] = min(left[0],self.arr[i+1].min)
                left[1] = max(left[1],self.arr[i+1].max)
                left[2] = left[2]+self.arr[i+1].sum
                lnum = lnum+num
            if j&1:
                right[0] = min(right[0],self.arr[j-1].min)
                right[1] = max(right[1],self.arr[j-1].max)
                right[2] = right[2]+self.arr[j-1].sum
                rnum = rnum + num
            i = i>>1
            j = j>>1
            num = num<<1
        res = [min(left[0] + self.arr[i].add, right[0] + self.arr[j].add)
            , max(left[1] + self.arr[i].add, right[1] + self.arr[j].add)
            , left[2] + right[2] + self.arr[i].add * lnum + self.arr[j].add * rnum]
        i = i >> 1
        while i > 0:
            res[0] += self.arr[i].add
            res[1] += self.arr[i].add
            res[2] += self.arr[i].add*(lnum+rnum)
            i = i>>1
        return res

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    t = ZKWSegmentTree(a)
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
