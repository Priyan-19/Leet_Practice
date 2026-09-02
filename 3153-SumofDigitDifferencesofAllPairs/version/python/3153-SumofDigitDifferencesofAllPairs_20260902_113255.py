# Last updated: 9/2/2026, 11:32:55 AM
1class Solution:
2    def sumDigitDifferences(self, nums: List[int]) -> int:
3        n = len(nums)
4        total = 0
5
6        # Find number of digits
7        digits = len(str(nums[0]))
8
9        for pos in range(digits):
10            count = [0] * 10
11
12            for num in nums:
13                digit = (num // (10 ** pos)) % 10
14                count[digit] += 1
15
16            for c in count:
17                total += c * (n - c)
18
19        return total // 2