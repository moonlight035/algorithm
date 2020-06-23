class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0],'.'}
        if len(p)>=2 and p[1] == '*':
            return self.isMatch(s,p[2:]) or (first_match and self.isMatch(s[1:],p))
        else:
            return first_match and self.isMatch(s[1:],p[1:])

    def otherIsMatch(self,s,p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def charMatch(i,j):
            if i<0:
                return False
            return p[j] in {s[i],'.'}

        m,n=len(s),len(p)
        if not p:
            return not s
        result = [[False]*(n+1) for _ in range(m+1)]
        result[0][0] = True
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1]!='*':
                    result[i][j] = (charMatch(i-1,j-1) and result[i-1][j-1])
                else:
                    if charMatch(i-1,j-2):
                        result[i][j] = result[i-1][j]
                    result[i][j]|= result[i][j-2]
        return result[m][n]

s = Solution()
print(s.otherIsMatch('aa','a*'))

