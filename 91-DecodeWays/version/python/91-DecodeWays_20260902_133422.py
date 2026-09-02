# Last updated: 9/2/2026, 1:34:22 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        if s[0] == '0':
4            return 0
5
6        prev2 = 1
7        prev1 = 1
8
9        for i in range(1, len(s)):
10            current = 0
11
12            # Take one digit
13            if s[i] != '0':
14                current += prev1
15
16            # Take two digits
17            two = int(s[i - 1:i + 1])
18
19            if 10 <= two <= 26:
20                current += prev2
21
22            prev2 = prev1
23            prev1 = current
24
25        return prev1
26        