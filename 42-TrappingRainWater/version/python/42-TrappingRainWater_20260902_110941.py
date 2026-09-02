# Last updated: 9/2/2026, 11:09:41 AM
1class Solution:
2    def longestValidParentheses(self, s: str) -> int:
3        stack = [-1]
4        maximum = 0
5
6        for i in range(len(s)):
7
8            if s[i] == '(':
9                stack.append(i)
10
11            else:
12                stack.pop()
13
14                if not stack:
15                    stack.append(i)
16                else:
17                    maximum = max(maximum, i - stack[-1])
18
19        return maximum