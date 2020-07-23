class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ' and r != 0 :
                return r
            elif s[i] != ' ':
                r += 1
        return r

