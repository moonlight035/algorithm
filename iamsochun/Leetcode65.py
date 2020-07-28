class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        dotflag = False #是否出现过 .
        eflag = False #是否出现过 e
        nflag = False #是否包含0-9
        zflag = False #是否出现过+-
        for i in s:
            if i in ('+','-'):
                if nflag or zflag:return False
                else:
                    zflag = True
            elif i == '.':
                if dotflag:return False
                else:
                    dotflag = True
                    zflag = True
            elif i == 'e':
                if eflag or (not nflag):return False
                else:
                    eflag = True
                    dotflag = True
                    nflag = False
                    zflag = False
            elif ord(i) >= ord('0') and ord(i) <= ord('9'):
                nflag = True
                continue
            else:return False
        return nflag
s = Solution()
print(s.isNumber(".-4"))

