from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = {}
        for i in strs:
            h = self.getHash(i)
            if t.get(h) is None:
                t[h] = []
            t[h].append(i)
        return list(t.values())


    def getHash(self, s: str) -> int:
        res = [0]*26
        for i in s:
            index = ord(i)-97
            res[index] += 1
        return tuple(res)

