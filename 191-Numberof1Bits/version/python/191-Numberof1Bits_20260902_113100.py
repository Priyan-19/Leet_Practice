# Last updated: 9/2/2026, 11:31:00 AM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        count = 0
4
5        while n:
6            count += n & 1
7            n >>= 1
8
9        return count