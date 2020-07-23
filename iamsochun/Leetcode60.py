class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = 1
        index = 0
        l = ''
        for i in range(n,0,-1):
            num *= n-i+1
            l = str(i)+l
            if num >= k:
                index = i
                break
        ans = ''
        k -= 1
        for i in range(len(l)):
            if k==0:
                ans = ans+l
                break
            num = num / (n-index+1-i)
            t = int(k//num)
            k -= t*num
            ans = ans + l[t]
            l = l[:t]+l[t+1:]
        for i in range(index-1,0,-1):
            ans = str(i)+ans
        return ans

    def other(self, n: int, k: int) -> str:
        factorials, nums = [1], ['1']
        for i in range(1, n):
            # generate factorial system bases 0!, 1!, ..., (n - 1)!
            factorials.append(factorials[i - 1] * i)
            # generate nums 1, 2, ..., n
            nums.append(str(i + 1))

        # fit k in the interval 0 ... (n! - 1)
        k -= 1

        # compute factorial representation of k
        output = []
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]

            output.append(nums[idx])
            del nums[idx]

        return ''.join(output)



s = Solution()
print(s.other(2,2))