# Last updated: 9/2/2026, 11:10:40 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3
4        stack = []
5
6        pairs = {
7            ')': '(',
8            ']': '[',
9            '}': '{'
10        }
11
12        for char in s:
13
14            if char in pairs:
15
16                if not stack or stack[-1] != pairs[char]:
17                    return False
18
19                stack.pop()
20
21            else:
22                stack.append(char)
23
24        return len(stack) == 0