# Last updated: 9/2/2026, 1:43:35 PM
1class Solution:
2    def largestInteger(self, num: int) -> int:
3        digits = list(str(num))
4
5        even = sorted(
6            [d for d in digits if int(d) % 2 == 0],
7            reverse=True
8        )
9
10        odd = sorted(
11            [d for d in digits if int(d) % 2 == 1],
12            reverse=True
13        )
14
15        e = 0
16        o = 0
17
18        for i in range(len(digits)):
19            if int(digits[i]) % 2 == 0:
20                digits[i] = even[e]
21                e += 1
22            else:
23                digits[i] = odd[o]
24                o += 1
25
26        return int(''.join(digits))