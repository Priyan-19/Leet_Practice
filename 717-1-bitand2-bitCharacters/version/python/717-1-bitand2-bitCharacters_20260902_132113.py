# Last updated: 9/2/2026, 1:21:13 PM
1class Solution:
2    def isOneBitCharacter(self, bits: List[int]) -> bool:
3        i = 0
4
5        while i < len(bits) - 1:
6            if bits[i] == 1:
7                i += 2
8            else:
9                i += 1
10
11        return i == len(bits) - 1