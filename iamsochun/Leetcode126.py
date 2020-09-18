import collections
import sys
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if beginWord not in wordList:
            wordList.append(beginWord)
        edgs = [[] for _ in range(len(wordList))]
        hash=collections.defaultdict(list)
        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                hash[wordList[i][:j]+'_'+wordList[i][j+1:]].append(i)

        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                edgs[i].extend(hash[wordList[i][:j]+ '_' + wordList[i][j+1:]])
            while i in edgs[i]:
                edgs[i].remove(i)
        idx = {}
        for i in range(len(wordList)):
            idx[wordList[i]] = i
        cost = [sys.maxsize] * len(wordList)
        cost[idx[beginWord]] = 0
        q = [[idx[beginWord]]]
        res = []
        while q:
            e = q.pop(0)
            last = e[-1]
            if wordList[last] == endWord:
                temp = []
                for i in e:
                    temp.append(wordList[i])
                res.append(temp)
            else:
                for l in edgs[last]:
                    if cost[last] + 1 <= cost[l]:
                        cost[l] = cost[last] + 1
                        x = e.copy()
                        x.append(l)
                        q.append(x)
        return res

    def distance(self, s: str, t: str):
        num = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                num += 1
                if num > 1:return False
        return num == 1

