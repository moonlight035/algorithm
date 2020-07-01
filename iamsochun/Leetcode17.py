class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []
        reflect = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
                   7: ['p', 'q', 'r', 's']
            , 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        res = reflect.get(int(digits[0]))
        for i in digits[1:]:
            temp = []
            for m in res:
                for n in reflect.get(int(i)):
                    temp.append(m+n)
            res = temp
        return res


s = Solution()
print(s.letterCombinations("23"))