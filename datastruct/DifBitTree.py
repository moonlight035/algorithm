class DifBitTree:
    def __init__(self,n):
        self.n = n
        self.arr1 = [0]*(n+1)
        self.arr2 = [0]*(n+1)

    def __nextIndex(self,i):
        return i&(-i)

    def getSum(self,m):
        sum = 0
        i = m+1
        while i > 0:
            sum += self.arr1[i]*(m+1)-self.arr2[i]
            i -= self.__nextIndex(i)
        return sum

    def getRangeSum(self,l,r):
        return self.getSum(r+1)-self.getRangeSum(l)

    def updateToTail(self,l,v):
        i = l+1
        while i <= self.n:
            self.arr1[i] += v
            self.arr2[i] += l*v
            i += self.__nextIndex(i)

    def updateRange(self,l,r,v):
        self.updateToTail(l,v)
        self.updateToTail(r+1,-v)

    def update(self,l,v):
        self.updateToTail(l,v)
        self.updateToTail(l+1,-v)

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    b = DifBitTree(len(a))
    for i in range(len(a)):
        if i > 0:
            b.updateToTail(i,a[i]-a[i-1])
        else:
            b.updateToTail(i,a[i])
    for i in range(len(a)):
        print(b.getSum(i))
    b.updateRange(0,3,4)
    print('---------------------')
    for i in range(len(a)):
        print(b.getSum(i))