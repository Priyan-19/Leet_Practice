# Last updated: 7/14/2026, 11:57:48 AM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n>1 and n%4==0:
            n//=4
        return n==1