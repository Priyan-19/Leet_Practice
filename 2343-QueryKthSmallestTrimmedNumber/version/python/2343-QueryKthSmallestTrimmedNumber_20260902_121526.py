# Last updated: 9/2/2026, 12:15:26 PM
1class Solution:
2    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
3        result = []
4
5        for k, trim in queries:
6            arr = []
7
8            for i, num in enumerate(nums):
9                trimmed = num[-trim:]
10                arr.append((trimmed, i))
11
12            arr.sort()
13
14            result.append(arr[k - 1][1])
15
16        return result