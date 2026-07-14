# Last updated: 7/14/2026, 11:58:17 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        te=0
        f=0
        s=1
        for i in range(1,n+1):
            c=f+s
            f=s
            s=c
        return c