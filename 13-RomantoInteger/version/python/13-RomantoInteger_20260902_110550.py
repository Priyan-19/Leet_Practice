# Last updated: 9/2/2026, 11:05:50 AM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3
4        values = {
5            "I": 1,
6            "V": 5,
7            "X": 10,
8            "L": 50,
9            "C": 100,
10            "D": 500,
11            "M": 1000
12        }
13
14        result = 0
15
16        for i in range(len(s)):
17
18            current = values[s[i]]
19
20            if i + 1 < len(s):
21                next_value = values[s[i + 1]]
22
23                if current < next_value:
24                    result -= current
25                else:
26                    result += current
27
28            else:
29                result += current
30
31        return result