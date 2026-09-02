# Last updated: 9/2/2026, 12:43:00 PM
1class Solution:
2    def hIndex(self, citations: List[int]) -> int:
3        citations.sort(reverse=True)
4
5        h = 0
6
7        for i, citation in enumerate(citations):
8            if citation >= i + 1:
9                h = i + 1
10            else:
11                break
12
13        return h