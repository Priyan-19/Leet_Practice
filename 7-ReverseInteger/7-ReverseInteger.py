# Last updated: 7/14/2026, 11:58:32 AM
class Solution:
    def reverse(self, x: int) -> int:
        si = -1 if x<0 else 1
        x = abs(x)
        s =0
        while x >0:
            ld = x %10
            s = 10*s +ld
            x//=10
            
        s=s*si
        if s < -2**31 or s > 2**31 - 1:
            return 0
        else :
            return s