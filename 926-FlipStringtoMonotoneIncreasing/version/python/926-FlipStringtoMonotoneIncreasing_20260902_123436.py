# Last updated: 9/2/2026, 12:34:36 PM
1class Solution:
2    def minFlipsMonoIncr(self, s: str) -> int:
3        ones = 0
4        flips = 0
5
6        for char in s:
7            if char == '1':
8                ones += 1
9            else:
10                flips = min(flips + 1, ones)
11
12        return flips