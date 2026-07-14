# Last updated: 7/14/2026, 11:57:22 AM
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n % 2==0:
            return n//2
        else:
            if n==1:
                return 0
            else :
                return n