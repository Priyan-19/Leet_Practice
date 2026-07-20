# Last updated: 7/20/2026, 2:24:49 PM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        l,r=0,len(s)-1
4        while(l<r):
5            s[l],s[r]=s[r],s[l]
6            l+=1
7            r-=1
8        