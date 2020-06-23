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
    def other(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]
a = [1,2,3,4]
print(1+int('0'))


