# Last updated: 9/2/2026, 1:22:36 PM
1class Solution:
2    def wiggleSort(self, nums: List[int]) -> None:
3        nums.sort()
4
5        n = len(nums)
6        mid = (n - 1) // 2
7        end = n - 1
8
9        result = []
10
11        while mid >= 0:
12            result.append(nums[mid])
13            mid -= 1
14
15            if end >= (n + 1) // 2:
16                result.append(nums[end])
17                end -= 1
18
19        nums[:] = result