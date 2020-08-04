class Solution:
    def minWindow(self, s: str, t: str) -> str:
        appear = {}
        for i in t:
            appear[i] = appear.get(i,0) + 1
        left = right = 0
        max = len(s) - 1
        resLeft = resRight = -1
        exits = {}
        while right <= max:
            if appear.get(s[right]) is not None:
                exits[s[right]] = exits.get(s[right],0) + 1
            while left <= right and self.exist(appear,exits):
                if resLeft == -1 or right - left < resRight - resLeft:
                    resLeft,resRight = left,right
                if appear.get(s[left]) is not None:
                    exits[s[left]] -= 1
                left += 1
            right += 1
        if resLeft == -1:
            return ""
        else:
            return s[resLeft:resRight+1]

    def exist(self,target:dict, src:dict):
        for i in target.keys():
            if src.get(i,0) < target[i]:
                return False
        return True