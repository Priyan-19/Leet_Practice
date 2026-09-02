# Last updated: 9/2/2026, 11:18:14 AM
1class Solution:
2    def duplicateNumbersXOR(self, nums: List[int]) -> int:
3        seen = set()
4        result = 0
5
6        for num in nums:
7            if num in seen:
8                result ^= num
9            else:
10                seen.add(num)
11
12        return result