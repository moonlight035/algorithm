class Solution:
    def minWindow(self, s: str, t: str) -> str:
        appear = {}
        for i in t:
            appear[i] = appear.get(i,0) + 1
        right = 0
        left = -1
        max = len(s) - 1
        resLeft = resRight = -1
        count = 0
        next = []
        nextIndex = 0
        while right <= max:
            if appear.get(s[right]) is not None:
                appear[s[right]] -= 1
                if appear[s[right]] >= 0:
                    count += 1
                next.append(right)
                if left == -1:
                    left = next[nextIndex]
                    nextIndex += 1
                while left <= right and count == len(t):
                    if left == right:
                        return s[left:right+1]
                    if resLeft == -1 or right - left < resRight - resLeft:
                        resLeft,resRight = left,right
                    appear[s[left]] += 1
                    if appear[s[left]] > 0:
                        count -= 1
                    left = next[nextIndex]
                    nextIndex += 1
            right += 1
        if resLeft == -1:
            return ""
        else:
            return s[resLeft:resRight+1]

s = Solution()
print(s.minWindow("ADOBECODEBANC","ABC"))