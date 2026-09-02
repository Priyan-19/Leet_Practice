# Last updated: 9/2/2026, 11:13:05 AM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3
4        n = len(nums)
5
6        for i in range(n):
7
8            while (
9                1 <= nums[i] <= n
10                and nums[nums[i] - 1] != nums[i]
11            ):
12
13                correct_index = nums[i] - 1
14
15                nums[i], nums[correct_index] = (
16                    nums[correct_index],
17                    nums[i]
18                )
19
20        for i in range(n):
21
22            if nums[i] != i + 1:
23                return i + 1
24
25        return n + 1