# Last updated: 7/20/2026, 11:28:33 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s= re.sub(r'[^A-Za-z0-9]', '',s).lower()
4
5        r=len(s)-1
6        l=0
7        so = True
8        if not s:
9            return True
10        while(l<r):
11            if s[l]==s[r]:
12                so=True
13                l+=1
14                r-=1
15            else:
16                so=False
17                break
18        if so==True:
19            return True
20        else :
21            return False