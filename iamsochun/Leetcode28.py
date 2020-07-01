
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        if len(haystack) < len(needle):
            return -1
        while i < len(haystack)-len(needle)+1:
            j = 0
            temp = i
            next = i+1
            while j<len(needle) and temp < len(haystack) and haystack[temp] == needle[j]:
                if  temp != i and haystack[next] != needle[0] and haystack[temp] == needle[0]:
                    next = temp
                temp = temp+1
                j = j+1
            if j == len(needle):
                return i
            i = next
        if len(needle) == 0:return 0
        else:return -1

    def other(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        res = [list(range(len(haystack)-len(needle)+1))]
        for i in range(0,len(needle)):
            next = []
            for j in res[i]:
                if j+i < len(haystack) and haystack[j+i] == needle[i]:
                    next.append(j)
            res.append(next)
        if len(res[len(needle)]) > 0:
            return res[len(needle)][0]
        else:
            return -1

    def kmp(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        quick = [None] *  (len(needle)+1)
        quick[0] = quick[1] = 0
        j = 2
        k = 0
        while j < len(needle):
            if needle[j-1] == needle[k]:
                k = k + 1
                quick[j] = k
                j = j + 1
            else:
                if k==0:
                    quick[j] = 0
                    j = j+1
                k = quick[k]

        m = 0
        n = 0
        start = 0
        while m<len(haystack) and n < len(needle):
            if haystack[m] == needle[n]:
                m = m+1
                n = n+1
            else:
                if n==0:
                    m = m+1
                    start = m
                else:
                    n = quick[n]
                    start = m-n
        if n == len(needle):
            return start
        else:
            return -1


    def kmpGreat(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        # 当needle的第index字符串不匹配时，对应下一个需要匹配的needle的index
        quick = [None] * (len(needle)+1)
        # -1代表haystack的当前字符无法与needle的第一个字符匹配，此时haystack的index自增1从下一个开始匹配
        quick[0] = -1
        j = 0
        k = -1
        # j代表当needle第j+1个字符不匹配，k指向第j个字符不匹配时quick值，动态规划
        while j < len(needle):
            if k == -1 or needle[j] == needle[k]:
                k = k + 1
                j = j + 1
                quick[j] = k
            else:
                # 此时可以看作后缀作为主字符串匹配needle时匹配失败，通过quick获取下一个需要匹配的index
                k = quick[k]

        m = 0
        n = 0
        start = 0
        while m < len(haystack) and n < len(needle):
            if n==-1 or  haystack[m] == needle[n]:
                m = m + 1
                n = n + 1
            else:
                n = quick[n]
                start = m - n
        if n == len(needle):
            return start
        else:
            return -1
s = Solution()
print(s.kmpGreat("mississippi","issip"))