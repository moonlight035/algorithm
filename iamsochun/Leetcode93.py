from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def done(site: int, index: int, temp: str):
            if index == 3:
                if site == len(s) - 1 or (s[site] != '0' and int(s[site:]) <= 255):
                    res.append(temp[1:]+'.'+s[site:])
                return
            if len(s) - site >= 4 - index:
                if s[site] == '0':
                    done(site+1, index+1, temp+'.0')
                else:
                    for i in range(site, len(s)-3+index):
                        if int(s[site:i+1]) <= 255:
                            done(i+1, index+1, temp+'.'+s[site:i+1])
                        else:
                            break
        done(0,0,'')
        return res