# Last updated: 9/2/2026, 1:37:06 PM
1class Solution:
2    def canBeValid(self, s: str, locked: str) -> bool:
3        n = len(s)
4
5        if n % 2 == 1:
6            return False
7
8        # Left → Right
9        balance = 0
10
11        for i in range(n):
12            if locked[i] == '0' or s[i] == '(':
13                balance += 1
14            else:
15                balance -= 1
16
17            if balance < 0:
18                return False
19
20        # Right → Left
21        balance = 0
22
23        for i in range(n - 1, -1, -1):
24            if locked[i] == '0' or s[i] == ')':
25                balance += 1
26            else:
27                balance -= 1
28
29            if balance < 0:
30                return False
31
32        return True