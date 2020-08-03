from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            end = i + 1
            l = len(words[i])
            while end < len(words):
                if l + len(words[end]) + 1 > maxWidth:
                    break
                l += len(words[end]) + 1
                end += 1
            blankNum = maxWidth - l
            end -= 1
            if end == len(words)-1:
                temp = [1]*(end-i+1)
                temp[-1] = blankNum
            elif end > i:
                temp = [1+blankNum//(end-i)]*(end-i+1)
                v = blankNum % (end - i)
                for k in range(v):
                    temp[k] += 1
                temp[-1] = 0
            else:
                temp = [blankNum]
            ans = ''
            for k in range(i, end+1):
                ans += words[k]+' '*temp[k-i]
            res.append(ans)
            i = end + 1
        return res

s = Solution()
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"],16))
