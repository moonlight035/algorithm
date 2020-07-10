
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        l = len(num)
        position = [[] for _ in range(10)]
        t = BitTree(l)
        for i in range(l):
            position[ord(num[i])-48].append(i)
            t.update(i,1)
        t.update(0,-1)
        next = [0]*10
        ans = ''
        i = 0
        while k > 0 and i < l:
            for j in range(10):
                if next[j] == len(position[j]):
                    continue
                index = t.getSum(position[j][next[j]])
                if index <= k:
                    k = k-index
                    ans += num[index]
                    num = num[:index]+num[index+1:]
                    i = i+1
                    t.update(position[j][next[j]],-1)
                    next[j] += 1
                    break
        return ans+num

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

s =Solution()
print(s.minInteger("234561",1))