# Last updated: 9/2/2026, 2:03:40 PM
1class Solution:
2    def getRow(self, rowIndex: int) -> List[int]:
3        row = [1] * (rowIndex + 1)
4
5        for i in range(1, rowIndex):
6            row[i] = row[i - 1] * (rowIndex - i + 1) // i
7
8        return row