from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        wordLen = len(words[0])
        i=0
        res=[]
        while i <= len(s)-wordLen*len(words):
            temp = i
            tempList = words.copy()
            while temp+wordLen<=len(s) and s[temp:temp+wordLen] in tempList:
                tempList.remove(s[temp:temp+wordLen])
                temp = temp+wordLen
            if not tempList:
                res.append(i)
            i = i+1
        return res

    def great(self, s: str, words: List[str]) -> List[int]:
        if not words or len(s) < len(words)*len(words[0]):
            return []
        wordLen = len(words[0])
        res=[]
        for i in range(wordLen):
            temp = j = i
            tempList = words.copy()
            while j <=  len(s)-wordLen*len(words):
                while temp + wordLen <= len(s) and s[temp:temp + wordLen] in tempList:
                    tempList.remove(s[temp:temp + wordLen])
                    temp = temp + wordLen
                if not tempList:
                    res.append(j)
                    tempList.append(s[j:j+wordLen])
                    j = j+wordLen
                elif s[temp:temp + wordLen] in s[j:temp]:
                    m = s.index(s[temp:temp + wordLen],j,temp)+wordLen
                    for k in range(j,m,wordLen):
                        tempList.append(s[k:k+wordLen])
                    j = m
                else:
                    j = temp+wordLen
                    temp = j
                    tempList = words.copy()
        return res

    def moreGreat(self, s: str, words: List[str]) -> List[int]:
        if not words or len(s) < len(words) * len(words[0]):
            return []
        wordLen = len(words[0])
        res = []
        all = {}
        for i in words:
            all[i] = all.get(i,0)+1
        for i in range(wordLen):
            temp = j = i
            d = all.copy()
            while j <= len(s) - wordLen * len(words):
                while temp + wordLen <= len(s) :
                    word = s[temp:temp + wordLen]
                    if d.get(word):
                        if d[word] == 1:
                            d.pop(word)
                        else:
                            d[word] = d[word]-1
                        temp = temp + wordLen
                    else:break
                if not d:
                    res.append(j)
                    word = s[j:j + wordLen]
                    d[word] = d.get(word,0)+1
                    j = j + wordLen
                elif s[temp:temp + wordLen] in s[j:temp]:
                    m = s.index(s[temp:temp + wordLen], j, temp) + wordLen
                    for k in range(j, m, wordLen):
                        word = s[k:k + wordLen]
                        d[word] = d.get(word,0)+1
                    j = m
                else:
                    j = temp + wordLen
                    temp = j
                    d = all.copy()
        return res

s = Solution()
print(s.moreGreat("cccab",["ca","cc"]))
# d = {}
# d[0] = d.get(0,0)+1
# print(d[0])
# print(bool(0))
# print(bool(1))
# print(bool(None))
# print()
