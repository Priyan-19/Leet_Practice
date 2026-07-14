# Last updated: 7/14/2026, 11:58:02 AM
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            te=0
            to=0
            te =n
            while(te>0):
                di=te%10
                to+=di*di
                te//=10
            n=to
        return n==1
