class Solution:
    def minInteger(self, num: str, k: int) -> str:
        r = ''
        i = 0
        while k > 0 and len(num) > 1:
            index = i
            for j in range(i+1,min(i+k+1,len(num))):
                if num[j] < num[index]:
                    index = j
                if num[j] == '0':
                    break
            r = r+num[index]
            num = num[:index] + num[index+1:]
            k = k - index + i
        return r+num

s = Solution()
print(s.minInteger('4321',4))