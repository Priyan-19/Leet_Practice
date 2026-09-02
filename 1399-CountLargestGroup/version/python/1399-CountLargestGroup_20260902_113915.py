# Last updated: 9/2/2026, 11:39:15 AM
1class Solution:
2    def countLargestGroup(self, n: int) -> int:
3        groups = {}
4
5        for num in range(1, n + 1):
6            digit_sum = sum(int(d) for d in str(num))
7
8            if digit_sum not in groups:
9                groups[digit_sum] = 0
10
11            groups[digit_sum] += 1
12
13        largest = max(groups.values())
14
15        return list(groups.values()).count(largest)