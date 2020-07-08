class ZKWSegmentTree:

    class Node:
        def __init__(self):
            self.min = 0
            self.max = 0
            self.sum = 0
            self.add = 0

    def __init__(self,n):
        i = 1
        while i < n+1:
            i = i<<1
        self.n = n
        self.base = i+1
        self.arr = [self.Node() for _ in range(i+n+2)]


    def __pushUp(self,i):
        i = i<<1
        num = 2
        while i > 0:
            left = self.arr[i<<1]
            right = self.arr[(i<<1)+1]
            now = self.arr[i]
            now.min = min(left.min,right.min)+now.add
            now.max = max(left.max,right.max)+now.add
            now.sum = left.sum + right.sum + now.add*num
            i = i<<1
            num = num<<1

    def update(self,i,v):
        self.arr[i + self.base].sum += v
        self.arr[i + self.base].min += v
        self.arr[i + self.base].max += v
        self.__pushUp(i+self.base)

    def updateRange(self,l,r,v):
        lnum, rnum, num = 0, 0, 1
        i = self.base+l-1
        j = self.base+r+1
        while i^j^1:
            if ~(i&1):
                self.arr[i+1].min += v
                self.arr[i+1].max += v
                self.arr[i+1].sum += num*v
                self.arr[i+1].add += v
                lnum += num
            if i > self.base:
                self.arr[i >> 1].min = min(self.arr[i>>1<<1].min,self.arr[i>>1<<1+1].min)+self.arr[i>>1].add
                self.arr[i >> 1].max = max(self.arr[i >> 1 << 1].max, self.arr[i >> 1 << 1 + 1].max)+self.arr[i>>1].add
            else:
                self.arr[i >> 1].min = self.arr[i>>1<<1+1].min
                self.arr[i >> 1].max = self.arr[i>>1<<1+1].max
            self.arr[i >> 1].sum = self.arr[i >> 1].sum+self.arr[i >> 1].add*lnum

            if j&1:
                self.arr[j-1].min += v
                self.arr[j-1].max += v
                self.arr[j-1].sum += num*v
                self.arr[j-1].add += v
                rnum += num
            if j < self.base + self.n - 2:
                self.arr[i >> 1].min = min(self.arr[i>>1<<1].min,self.arr[i>>1<<1+1].min)+self.arr[i>>1].add
                self.arr[i >> 1].max = max(self.arr[i >> 1 << 1].max, self.arr[i >> 1 << 1 + 1].max)+self.arr[i>>1].add
            else:
                self.arr[i >> 1].min = self.arr[i>>1<<1+1].min
                self.arr[i >> 1].max = self.arr[i>>1<<1+1].max
            self.arr[i >> 1].sum = self.arr[i >> 1].sum+self.arr[i >> 1].add*lnum

    def getRange(self,l,r):
        lnum,rnum,num = 0,0,1
        left,right = [0,0,0],[0,0,0]
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
            if ~(i&1):
                if ~lnum:
                    left[0] = self.arr[i+1].min
                    left[1] = self.arr[i+1].max
                    left[2] = self.arr[i+1].sum
                else:
                    left[0] = min(left[0],self.arr[i+1].min)
                    left[1] = max(left[1],self.arr[i+1].max)
                    left[2] = left[2]+self.arr[i+1].sum
                lnum = lnum+num
            if j&1:
                if ~rnum:
                    right[0] = self.arr[j-1].min
                    right[1] = self.arr[j-1].max
                    right[2] = self.arr[j-1].sum
                else:
                    right[0] = min(right[0],self.arr[j-1].min)
                    right[1] = max(right[1],self.arr[j-1].max)
                    right[2] = right[2]+self.arr[j-1].sum
                rnum = rnum + num
            i = i>>1
            j = j>>1
            num = num<<1
        res = [min(left[0],right[0]), max(left[1],right[1]), left[0]+right[0]]
        i = i >> 1
        while i > 0:
            res[0] += self.arr[i].add
            res[1] += self.arr[i].add
            res[2] += self.arr[i].add*(lnum+rnum)
        return res

