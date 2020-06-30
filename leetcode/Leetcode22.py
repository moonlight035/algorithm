class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def digui(s,i,count):
            if count == n:
                res.append(s+')'*(2*n-i+1))
            else:
                if count < n:
                    digui(s+'(',i+1,count+1)
                if count>i-1-count:
                    digui(s+')',i+1,count)
        digui('',1,0)
        return res
s = Solution()
print(s.generateParenthesis(3))
print('asd'+'as'*3)