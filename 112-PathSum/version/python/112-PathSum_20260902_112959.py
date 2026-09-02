# Last updated: 9/2/2026, 11:29:59 AM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        result = 0
4
5        for _ in range(32):
6            result = (result << 1) | (n & 1)
7            n >>= 1
8
9        return result