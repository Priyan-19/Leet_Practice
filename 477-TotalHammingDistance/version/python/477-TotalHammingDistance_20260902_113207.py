# Last updated: 9/2/2026, 11:32:07 AM
1class Solution:
2    def totalHammingDistance(self, nums: List[int]) -> int:
3        total = 0
4
5        for bit in range(32):
6            ones = 0
7
8            for num in nums:
9                if num & (1 << bit):
10                    ones += 1
11
12            zeros = len(nums) - ones
13
14            total += ones * zeros
15
16        return total