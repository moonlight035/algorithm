import collections
from typing import List, Dict


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        left = collections.defaultdict(list)
        right = collections.defaultdict(list)
        res = []
        for i in range(len(words)):
            word = words[i]
            left[word[::-1]].append(i)
            right[word[::-1]].append(i)
            self.handle(word,left,right,i)
        for i in range(len(words)):
            for j in left[words[i]]:
                if i != j and (words[i] != words[j][::-1] or j > i):
                    res.append([j,i])
            for j in right[words[i]]:
                if i != j and (words[i] != words[j][::-1] or j > i):
                    res.append([i,j])
        return res


    def handle(self, word: str, left: Dict[str,list], right: Dict[str,list], index: int):
        l = len(word)
        i = 0
        while i < l:
            if word[i] == word[l-1]:
                j = l-1
                k = i
                while k < j and word[k] == word[j]:
                    j -= 1
                    k += 1
                if word[k] == word[j]:
                    if i == 0:
                        left[''].append(index)
                    else:
                        left[word[i-1::-1]].append(index)
            i += 1
        i = l - 1
        while i >= 0:
            if word[i] == word[0]:
                j = 0
                k = i
                while j < k and word[k] == word[j]:
                    j += 1
                    k -= 1
                if word[k] == word[j]:
                    right[word[:i:-1]].append(index)
            i -= 1

    def other(self, words: List[str]) -> List[List[int]]:
        def findWord(s: str, left: int, right: int) -> int:
            return indices.get(s[left:right + 1], -1)

        def isPalindrome(s: str, left: int, right: int) -> bool:
            sub = s[left:right+1]
            return sub == sub[::-1]

        n = len(words)
        indices = {word[::-1]: i for i, word in enumerate(words)}

        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])

        return ret

    def another(self, words: List[str]) -> List[List[int]]:

        tree1 = TrieTree()
        tree2 = TrieTree()
        for i in range(len(words)):
            tree1.insert(words[i][::-1], i)
            tree2.insert(words[i],i)
        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            res = self.manacher(word)
            left = tree1.search(word)
            right = tree2.search(word[::-1])
            for j in range(m + 1):
                if res[j + m] == m - j:
                    leftId = left[j]
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and res[j] == j:
                    rightId = right[m - j]
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])

        return ret

    def manacher(self, s: str) -> List[int]:
        t = '#' + '#'.join(s) + '#'
        res = [1] * len(t)
        pos = maxHeight = -1
        for i in range(len(t)):
            if i < maxHeight:
                res[i] = min(res[2 * pos - i], maxHeight - i + 1)
            else:
                res[i] = 1
            while i + res[i] < len(t) and i - res[i] >= 0 and t[i + res[i]] == t[i - res[i]]:
                res[i] += 1

            if res[i] + i - 1 > maxHeight:
                pos = i
                maxHeight = res[i] + i - 1
        return [i-1 for i in res]

class Node:
    def __init__(self):
        self.index = -1
        self.prefix = 0
        self.next = None

class TrieTree:
    def __init__(self):
        self.root = Node()
        self.root.next = [Node() for _ in range(26)]

    def insert(self, s: str, index: int):
        if s == '':
            self.root.index = index
        temp = self.root.next
        for i in range(len(s)):
            temp[ord(s[i])-97].prefix += 1
            if i == len(s)-1:
                temp[ord(s[i]) - 97].index = index
            else:
                if temp[ord(s[i])-97].next is None:
                    temp[ord(s[i]) - 97].next = [Node() for _ in range(26)]
                temp = temp[ord(s[i]) - 97].next

    def search(self, s: str):
        res = [-1]*(len(s)+1)
        res[0] = self.root.index
        temp = self.root.next
        for i in range(len(s)):
            res[i+1] = temp[ord(s[i])-97].index
            if temp[ord(s[i])-97].prefix == 0 or not temp[ord(s[i])-97].next:
                break
            temp = temp[ord(s[i])-97].next
        return res



s = Solution()
print(s.another(["abcd","dcba","lls","s","sssll"]))
