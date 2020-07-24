class Solution:
    def divisorGame(self, N: int) -> bool:
        res = [False]*N
        for i in range(2,N+1):
            for j in range(1,i//2+1):
                if i%j == 0:
                    res[i-1] = res[i-1] | (~res[i-j-1])
                    if res[i-1]:break
        return res[N-1]

    def other(self, N: int) -> bool:
        return N%2==0