from typing import List

# 求最长回文子串
def manacher(s: str) -> List[int]:
    t = '#'+'#'.join(s)+'#'
    res = [1]*len(t)
    pos = maxHeight = -1
    for i in range(len(t)):
        if i < maxHeight:
            res[i] = min(res[2*pos - i], maxHeight - i + 1)
        else:
            res[i] = 1
        while i + res[i] < len(t) and i - res[i] >= 0 and t[i+res[i]] == t[i - res[i]]:
            res[i] += 1

        if res[i] + i - 1 > maxHeight:
            pos = i
            maxHeight = res[i] + i - 1
    return res
s = 'abba'
print(manacher(s))