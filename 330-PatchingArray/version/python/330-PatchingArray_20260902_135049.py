# Last updated: 9/2/2026, 1:50:49 PM
1class Solution:
2    def minPatches(self, nums: List[int], n: int) -> int:
3        miss = 1
4        patches = 0
5        i = 0
6
7        while miss <= n:
8            if i < len(nums) and nums[i] <= miss:
9                miss += nums[i]
10                i += 1
11            else:
12                miss += miss
13                patches += 1
14
15        return patches
16        