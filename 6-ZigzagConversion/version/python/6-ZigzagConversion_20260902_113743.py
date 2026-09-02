# Last updated: 9/2/2026, 11:37:43 AM
1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1 or numRows >= len(s):
4            return s
5
6        rows = [""] * numRows
7        row = 0
8        direction = 1
9
10        for char in s:
11            rows[row] += char
12
13            if row == 0:
14                direction = 1
15            elif row == numRows - 1:
16                direction = -1
17
18            row += direction
19
20        return "".join(rows)