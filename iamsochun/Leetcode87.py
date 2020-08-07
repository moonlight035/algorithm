import collections
from copy import deepcopy

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        data = collections.defaultdict(list)
        for i in range(len(s1)):
            data[s1[i]].append(i)
        max = 0
        status = 0
        cache = deepcopy(data)
        for i in range(len(s2)):
            if cache[s2[i]]:
                index = cache[s2[i]].pop(0)
            else:
                return False
            status += 1 << index
            if max < index:
                max = index
            elif status == (1 << (max+1))  - 1:
                break
        if max != len(s2) - 1 and self.isScramble(s1[:max+1],s2[:max+1]) and self.isScramble(s1[max+1:],s2[max+1:]):
            return True

        min = len(s2) - 1
        status = 0
        cache = deepcopy(data)
        for i in range(len(s2)):
            if cache[s2[i]]:
                index = cache[s2[i]].pop()
            else:
                return False
            status += 1 << (len(s2) - 1 - index)
            if min > index:
                min = index
            elif status == (1 << (len(s2)-min))  - 1:
                break
        if min != 0 and self.isScramble(s1[min:],s2[:len(s1)-min]) and self.isScramble(s1[:min],s2[len(s1)-min:]):
            return True
        return False

    def other(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        cache1 = collections.defaultdict(list)
        cache2 = collections.defaultdict(list)
        for i in range(len(s1)):
            cache1[s1[i]].append(i)
            cache2[s1[i]].append(i)
        max = 0
        statusMax = 0
        maxFlag = True
        min = len(s2) - 1
        statusMin = 0
        minFlag = True
        for i in range(len(s2)):
            if not minFlag and not maxFlag:
                break
            if maxFlag:
                if cache1[s2[i]]:
                    index = cache1[s2[i]].pop(0)
                else:
                    return False
                statusMax += 1 << index
                if max < index:
                    max = index
                elif statusMax == (1 << (max + 1)) - 1:
                    maxFlag = False
            if minFlag:
                if cache2[s2[i]]:
                    index = cache2[s2[i]].pop()
                else:
                    return False
                statusMin += 1 << (len(s2) - 1 - index)
                if min > index:
                    min = index
                elif statusMin == (1 << (len(s2) - min)) - 1:
                    minFlag = False
        if max != len(s2) - 1 and self.isScramble(s1[:max + 1], s2[:max + 1]) and self.isScramble(s1[max + 1:],s2[max + 1:]):
            return True
        if min != 0 and self.isScramble(s1[min:], s2[:len(s1) - min]) and self.isScramble(s1[:min], s2[len(s1) - min:]):
            return True
        return False

    def another(self, s1: str, s2: str) -> bool:
        l = len(s1)
        dp = [[[False]*l for _ in range(l)] for _ in range(l)]
        for i in range(l):
            for j in range(l):
                dp[i][j][0] = s1[i] == s2[j]

        for ll in range(1,l):
            for i in range(0,l - ll):
                for j in range(0, l - ll):
                    for k in range(1,ll+1):
                        if (dp[i][j][k-1] and dp[i+k][j+k][ll+1-k-1]) or (dp[i][j+ll-k][k-1] and dp[i+k][j][ll+1-k-1]):
                            dp[i][j][ll] = True
                            break
        return dp[0][0][l-1]



s = Solution()
print(s.another("atzzffqpnwcxhejzjsnpmkmzngneo","acegneonzmkmpnsjzjhxwnpqffzzt"))
print(s.other("atzzffqpnwcxhejzjsnpmkmzngneo","acegneonzmkmpnsjzjhxwnpqffzzt"))