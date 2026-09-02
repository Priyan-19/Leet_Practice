# Last updated: 9/2/2026, 12:10:41 PM
1class Solution:
2    def maxScore(self, nums: List[int], x: int) -> int:
3        even = float('-inf')
4        odd = float('-inf')
5
6        if nums[0] % 2 == 0:
7            even = nums[0]
8        else:
9            odd = nums[0]
10
11        for num in nums[1:]:
12            if num % 2 == 0:
13                even = max(
14                    even + num,
15                    odd + num - x
16                )
17            else:
18                odd = max(
19                    odd + num,
20                    even + num - x
21                )
22
23        return max(even, odd)