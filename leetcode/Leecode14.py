class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        s = strs[0]
        for i in strs[1:]:
            x = min(len(s),len(i))
            if x==0:
                s = ''
                break;
            for j in range(x):
                if s[j] != i[j]:
                    j-=1;
                    break;
            s = s[:j+1]
        return s;

