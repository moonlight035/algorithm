class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0]
        l1 = len(num1)
        l2 = len(num2)
        for i in range(l1-1,-1,-1):
            for j in range(l2-1,-1,-1):
                index = l1+l2-i-j-2
                x = (ord(num1[i])-48)*(ord(num2[j])-48)+res[index]
                head = x // 10
                res[index] = x % 10
                if index+1 > len(res)-1:
                    res.append(head)
                else:
                    res[index+1] = res[index+1]+head
        while res[-1] == 0 and len(res) > 1:
            res.pop()
        return ''.join(reversed([chr(i+48) for i in res]))



s = Solution()
print(s.multiply("123","456"))
