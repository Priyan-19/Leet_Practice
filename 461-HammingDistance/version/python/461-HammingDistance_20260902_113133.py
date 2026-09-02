# Last updated: 9/2/2026, 11:31:33 AM
1class Solution:
2    def hammingDistance(self, x: int, y: int) -> int:
3        xor = x ^ y
4        count = 0
5
6        while xor:
7            count += xor & 1
8            xor >>= 1
9
10        return count