# Last updated: 7/14/2026, 11:57:34 AM
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        co= {"a":0 ,"b":0,"c":0}
        l=0
        re=0
        for r in range(len(s)):
            co[s[r]]+=1
            while co["a"] >0 and co["b"] > 0 and co["c"] >0:
                re += len(s)-r
                co[s[l]]-=1
                l+=1
        return re
