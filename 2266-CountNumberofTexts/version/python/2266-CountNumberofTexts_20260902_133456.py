# Last updated: 9/2/2026, 1:34:56 PM
1class Solution:
2    def countTexts(self, pressedKeys: str) -> int:
3        MOD = 10**9 + 7
4        n = len(pressedKeys)
5
6        dp = [0] * (n + 1)
7        dp[0] = 1
8
9        for i in range(1, n + 1):
10            # Press current key once
11            dp[i] = dp[i - 1]
12
13            # Press current key twice
14            if i >= 2 and pressedKeys[i - 1] == pressedKeys[i - 2]:
15                dp[i] += dp[i - 2]
16
17            # Press current key three times
18            if i >= 3 and pressedKeys[i - 1] == pressedKeys[i - 2] == pressedKeys[i - 3]:
19                dp[i] += dp[i - 3]
20
21            # 7 and 9 can be pressed four times
22            if (pressedKeys[i - 1] == '7' or pressedKeys[i - 1] == '9'):
23                if i >= 4 and pressedKeys[i - 1] == pressedKeys[i - 2] == pressedKeys[i - 3] == pressedKeys[i - 4]:
24                    dp[i] += dp[i - 4]
25
26            dp[i] %= MOD
27
28        return dp[n]