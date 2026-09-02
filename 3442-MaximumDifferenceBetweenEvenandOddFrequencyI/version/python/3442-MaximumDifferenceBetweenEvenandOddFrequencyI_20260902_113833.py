# Last updated: 9/2/2026, 11:38:33 AM
1from collections import Counter
2
3class Solution:
4    def maxDifference(self, s: str) -> int:
5        freq = Counter(s)
6
7        odd = []
8        even = []
9
10        for count in freq.values():
11            if count % 2 == 1:
12                odd.append(count)
13            else:
14                even.append(count)
15
16        return max(odd) - min(even)