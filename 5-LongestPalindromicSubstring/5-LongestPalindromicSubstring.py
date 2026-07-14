# Last updated: 7/14/2026, 11:58:34 AM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        re=""
        for i in range(n):
            for j in range(i+1,n+1):
                r=s[i:j]
                if r==r[::-1] and len(r)>len(re):
                    re=r
        return(re)
        