class Solution:
    def climbStairs(self, n: int) -> int:
        te=0
        if n==1:
            return 1
        elif n==2:
            return 2
        else :
            f=1
            s=2
            for i in range(3,n+1):
                c=f+s
                f=s
                s=c
            te=c
        return (te)