class SegmentTree:

    class Node:
        def __init__(self, l: int, r: int, parent):
            self.l = l
            self.r = r
            self.lchild = None
            self.rchild = None
            self.parent = parent
            self.min = 0
            self.max = 0
            self.sum = 0
            self.down = 0

    def __init__(self,n):
        self.n = n
        self.root = self.build(0, n-1, None)

    def build(self,l,r,parent):
        if l == r:
            return self.Node(l,r,parent)
        mid = (l+r)//2
        n = self.Node(l,r,parent)
        n.lchild = self.build(l,mid,n)
        n.rchild = self.build(mid+1,r,n)
        return n

    def update(self,i,v):
        if i >= self.n:
            return
        temp = self.root
        while not temp.l == temp.r:
            self.__pushDown(temp)
            mid = (temp.l+temp.r)//2
            if i <= mid:temp = temp.lchild
            else:temp = temp.rchild
        temp.sum += v
        temp.min += v
        temp.max += v
        self.__pushUp(temp)


    def __pushDown(self, temp: Node):
        if temp.down != 0:
            lchild = temp.lchild
            rchild = temp.rchild
            if lchild is not None:
                lchild.min += temp.down
                lchild.max += temp.down
                lchild.sum += temp.down*(lchild.r - lchild.l+1)
                lchild.down = temp.down
            if rchild is not None:
                rchild.min += temp.down
                rchild.max += temp.down
                rchild.sum += temp.down*(rchild.r - rchild.l+1)
                rchild.down = temp.down
            temp.down = 0

    def __pushUp(self, start: Node):
        temp = start.parent
        while temp is not None:
            temp.sum = temp.lchild.sum+temp.rchild.sum
            temp.min = min(temp.lchild.min,temp.rchild.min)
            temp.max = max(temp.lchild.max,temp.rchild.max)
            temp = temp.parent

    def __doRangeUpdate(self,temp,l,r,v):
        if temp.l == l and temp.r == r:
            temp.sum += v*(temp.r - temp.l + 1)
            temp.min += v
            temp.max += v
            temp.down += v
            return
        self.__pushDown(temp)
        mid = (temp.l+temp.r)//2
        if l<= mid and r>mid:
            self.__doRangeUpdate(temp.lchild,l,mid,v)
            self.__doRangeUpdate(temp.rchild,mid+1,r,v)
        elif l > mid:
            self.__doRangeUpdate(temp.rchild,l,r,v)
        else:
            self.__doRangeUpdate(temp.lchild,l,r,v)
        temp.min = min(temp.lchild.min,temp.rchild.min)
        temp.max = max(temp.lchild.max, temp.rchild.max)
        temp.sum = temp.lchild.sum + temp.rchild.sum

    def updateRange(self,l,r,v):
        self.__doRangeUpdate(self.root,l,r,v)

    def __doGetRange(self,temp,l,r):
        if r >= self.n or l < 0:
            return []
        if temp.l == l and temp.r == r:
            return [temp.min, temp.max, temp.sum]
        self.__pushDown(temp)
        mid = (temp.l + temp.r) // 2
        if l<= mid and r>mid:
            left = self.__doGetRange(temp.lchild,l,mid)
            right = self.__doGetRange(temp.rchild,mid+1,r)
            return [min(left[0],right[0]),max(left[1],right[1]),left[2]+right[2]]
        elif l > mid:
            return self.__doGetRange(temp.rchild,l,r)
        else:
            return self.__doGetRange(temp.lchild,l,r)

    def getRange(self,l,r):
        return self.__doGetRange(self.root, l, r )



if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    t = SegmentTree(len(a))
    for i in range(len(a)):
        t.update(i,a[i])
    for i in range(len(a)):
        print(t.getRange(0, i))
    print('```````````````````````````````````')
    for i in range(len(a)):
        print(t.getRange(i, len(a) - 1))
    t.updateRange(0, 3, 8)
    print('````````````````````````````````````')
    for i in range(len(a)):
        print(t.getRange(0, i))
    print('`````````````````````````````````````````')
    t.update(6, 8)
    for i in range(len(a)):
        print(t.getRange(0, i))



        #12