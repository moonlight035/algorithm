class Solution:
    def countAndSay(self, n: int) -> str:
        res = ['1']
        for i in range(1,n):
            num = 1
            next = []
            j = 1
            while j <= len(res):
                if j <len(res) and res[j] == res[j-1]:
                    num = num+1
                else:
                    next.append(str(num))
                    next.append(res[j-1])
                    num = 1
                j = j+1
            res = next
        return ''.join(res)


s = Solution()
print(s.countAndSay(6))
