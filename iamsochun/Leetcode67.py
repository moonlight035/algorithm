class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m,n = len(a),len(b)
        result = ['0']
        for i,j in zip(range(m-1,-1,-1),range(n-1,-1,-1)):
            if (int(result[0]) + int(a[i]) + int(b[j])) > 1:
                result.insert(0,'1')
            else:
                result.insert(0,'0')
            result[1] = str(int(result[1]) ^ int(a[i]) ^ int(b[j]))
        for i in range(abs(m-n)-1,-1,-1):
            x = a[i] if m>n else b[i]
            if (int(result[0]) + int(x)) > 1:
                result.insert(0,'1')
            else:
                result.insert(0,'0')
            result[1] = str(int(x) ^ int(result[1]))
        if result[0]=='0':
            result.pop(0)
        return ''.join(result)


    def other(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        res = ['0']*max(la,lb)
        i,j,next=la-1,lb-1,0
        while i >= 0 or j >= 0:
            va = ord(a[i])-48 if i>=0 else 0
            vb = ord(b[j])-48 if j>=0 else 0
            v = va + vb + next
            if v > 1:
                next = 1
                v = v%2
            else:
                next = 0
            res[max(i,j)] = str(v)
            i -= 1
            j -= 1
        if next == 1:
            res.insert(0,'1')
        return ''.join(res)

s = Solution()
print(s.other("1010","1011"))


