# Last updated: 9/2/2026, 1:39:20 PM
1class Solution:
2    def makeLargestSpecial(self, s: str) -> str:
3        parts = []
4        count = 0
5        start = 0
6
7        for i, char in enumerate(s):
8            if char == '1':
9                count += 1
10            else:
11                count -= 1
12
13            if count == 0:
14                inner = s[start + 1:i]
15                largest = self.makeLargestSpecial(inner)
16                parts.append('1' + largest + '0')
17                start = i + 1
18
19        parts.sort(reverse=True)
20
21        return ''.join(parts)