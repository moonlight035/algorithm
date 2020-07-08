import math
from typing import List


def RMQ(nums: List[int]) -> List[List[int]]:
    l = len(nums)
    max = math.floor(math.log2(l))
    dp = [[0]*(max+1) for _ in range(l)]

    for i in range(l):
        dp[i][0] = nums[i]

    for i in range(1,max+1):
        for j in range(l+1-(1<<i)):
            dp[j][i] = min(dp[j][i-1],dp[j+(1<<(i-1))][i-1])

    return dp

x = [1,3,2,54,6,4,654,65,46,54,64,6,4,64]
dp = RMQ(x)
res = [[None]*len(x) for _ in range(len(x))]
for i in range(len(x)):
    for j in range(i,len(x)):
        max = math.floor(math.log2(j-i+1))
        res[i][j] = min(dp[i][max],dp[j+1-(1 << max)][max])
print(res)