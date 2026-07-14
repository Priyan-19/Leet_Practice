# Last updated: 7/14/2026, 11:57:57 AM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        min_val = (float('-inf'))
        return n>0 and n & (n-1)==0

        