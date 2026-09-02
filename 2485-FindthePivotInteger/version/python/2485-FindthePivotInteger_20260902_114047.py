# Last updated: 9/2/2026, 11:40:47 AM
1class Solution:
2    def pivotInteger(self, n: int) -> int:
3        total = n * (n + 1) // 2
4
5        x = int(total ** 0.5)
6
7        if x * x == total:
8            return x
9
10        return -1