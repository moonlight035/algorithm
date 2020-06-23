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

s = Solution()
print(s.isValid("()"))