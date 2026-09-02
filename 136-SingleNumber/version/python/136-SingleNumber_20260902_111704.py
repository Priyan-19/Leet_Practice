# Last updated: 9/2/2026, 11:17:04 AM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        result = 0
4
5        for num in nums:
6            result ^= num
7
8        return result