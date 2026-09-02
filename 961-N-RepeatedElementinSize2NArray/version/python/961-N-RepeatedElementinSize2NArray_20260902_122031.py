# Last updated: 9/2/2026, 12:20:31 PM
1class Solution:
2    def repeatedNTimes(self, nums: List[int]) -> int:
3        seen = set()
4
5        for num in nums:
6            if num in seen:
7                return num
8
9            seen.add(num)