# Last updated: 9/2/2026, 1:45:45 PM
1class Solution:
2    def getMaximumConsecutive(self, coins: List[int]) -> int:
3        coins.sort()
4
5        reach = 0
6
7        for coin in coins:
8            if coin > reach + 1:
9                break
10
11            reach += coin
12
13        return reach + 1
14        