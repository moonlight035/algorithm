class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        v = ''
        i = 0
        while i <= len(path):
            if (i == len(path) or path[i] == '/') and v != '':
                if v == '..' and len(res) > 0:
                    res.pop()
                elif v != '.' and v != '..':
                    res.append(v)
                v = ''
            elif i < len(path) and path[i] != '/':
                v += path[i]
            i += 1
        return '/'+'/'.join(res)

s = Solution()
print(s.simplifyPath("/home/"))
