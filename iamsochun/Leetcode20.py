class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'}':'{',']':'[',')':'('}
        stack = []
        for i in s:
            if d.get(i) is not None:
                if len(stack)==0 or stack.pop()!=d[i]:return False
            else:
                stack.append(i)
        if len(stack)==0:
            return True
        else:
            return False
    def other(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'}': '{', ']': '[', ')': '('}
        l = list(s)
        a=-1
        for i in range(len(l)):
            if d.get(l[i]) is None:
                a = a+1
                l[a] = l[i]
            elif a < 0 or d.get(l[i]) != l[a]:
                return False
            else:
                a = a-1
        if a==-1:
            return True
        else:
            return False

s = Solution()
print(s.other("("))