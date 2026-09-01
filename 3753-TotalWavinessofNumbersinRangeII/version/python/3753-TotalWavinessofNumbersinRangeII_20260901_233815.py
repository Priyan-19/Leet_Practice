# Last updated: 9/1/2026, 11:38:15 PM
1class Solution:
2    def totalWaviness(self, num1: int, num2: int) -> int:
3
4        def calc(num):
5            if num < 100:
6                return 0
7
8            s = str(num)
9            dp = {}
10
11            def solve(idx, pp, p, tight, lead):
12                if idx == len(s):
13                    return (1, 0)
14
15                key = (idx, pp, p, tight, lead)
16                if key in dp:
17                    return dp[key]
18
19                cnt = 0
20                wave = 0
21
22                lim = int(s[idx]) if tight else 9
23
24                for d in range(lim + 1):
25                    ntight = tight and (d == lim)
26                    nlead = lead and (d == 0)
27
28                    np = 10 if nlead else d
29                    npp = 10 if nlead else (10 if lead else p)
30
31                    wavy = False
32                    if pp != 10 and p != 10:
33                        if (pp < p > d) or (pp > p < d):
34                            wavy = True
35
36                    c, w = solve(idx + 1, npp, np, ntight, nlead)
37
38                    cnt += c
39                    wave += w + (c if wavy else 0)
40
41                dp[key] = (cnt, wave)
42                return dp[key]
43
44            return solve(0, 10, 10, True, True)[1]
45
46        return calc(num2) - calc(num1 - 1)