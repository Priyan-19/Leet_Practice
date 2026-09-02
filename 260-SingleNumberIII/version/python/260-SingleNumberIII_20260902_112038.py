# Last updated: 9/2/2026, 11:20:38 AM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> List[int]:
3        xor = 0
4
5        for num in nums:
6            xor ^= num
7
8        diff = xor & -xor
9
10        a = 0
11        b = 0
12
13        for num in nums:
14            if num & diff:
15                a ^= num
16            else:
17                b ^= num
18
19        return [a, b]