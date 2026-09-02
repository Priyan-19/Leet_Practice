# Last updated: 9/2/2026, 12:36:08 PM
1class Solution:
2    def minimumCost(self, s: str) -> int:
3        n = len(s)
4        cost = 0
5
6        for i in range(n - 1):
7            if s[i] != s[i + 1]:
8                cost += min(i + 1, n - i - 1)
9
10        return cost