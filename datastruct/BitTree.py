class BitTree:
    def __init__(self,n):
        self.n = n
        self.arr = [0]*(n+1)

    def __nextIndex(self,i):
        return i&(-i)

    def getSum(self,m):
        sum = 0
        m = m+1
        while m > 0:
            sum += self.arr[m]
            m -= self.__nextIndex(m)
        return sum

    def getRangeSum(self,l,r):
        r = r+1
        return self.getSum(r)-self.getSum(l)

    def update(self,i,v):
        i = i+1
        while i <= self.n:
            self.arr[i] += v
            i += self.__nextIndex(i)

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    b = BitTree(len(a))
    for i in range(len(a)):
        b.update(i,a[i])
    for i in range(len(a)):
        print(b.getSum(i))