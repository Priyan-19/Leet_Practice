# Last updated: 7/14/2026, 11:57:50 AM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1 and n % 3 == 0:
            n //= 3
        return n == 1