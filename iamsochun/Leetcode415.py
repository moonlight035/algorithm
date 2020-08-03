class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ['0']*(max(len(num1),len(num2))+1)
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 or j >= 0:
            v1 = ord(num1[i])-48 if i >=0 else 0
            v2 = ord(num2[j]) - 48 if j >= 0 else 0
            index = max(i,j)+1
            v = ord(res[index])-48 + v1 + v2
            res[index] = str(v%10)
            if v >= 10:
                res[index-1] = '1'
            i -= 1
            j -= 1
        if res[0] == '0':
            res.pop(0)
        return ''.join(res)

s = Solution()
print(s.addStrings("0",'9'))