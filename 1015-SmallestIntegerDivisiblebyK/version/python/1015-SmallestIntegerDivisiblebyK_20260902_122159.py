# Last updated: 9/2/2026, 12:21:59 PM
1class Solution:
2    def smallestRepunitDivByK(self, k: int) -> int:
3        if k % 2 == 0 or k % 5 == 0:
4            return -1
5
6        remainder = 0
7
8        for length in range(1, k + 1):
9            remainder = (remainder * 10 + 1) % k
10
11            if remainder == 0:
12                return length
13
14        return -1