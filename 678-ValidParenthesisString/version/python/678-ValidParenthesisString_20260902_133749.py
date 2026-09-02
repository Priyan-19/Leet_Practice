# Last updated: 9/2/2026, 1:37:49 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        low = 0
4        high = 0
5
6        for char in s:
7            if char == '(':
8                low += 1
9                high += 1
10
11            elif char == ')':
12                low -= 1
13                high -= 1
14
15            else:  
16                low -= 1       
17                high += 1     
18
19            if high < 0:
20                return False
21
22            low = max(low, 0)
23
24        return low == 0