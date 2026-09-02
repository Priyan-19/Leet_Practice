# Last updated: 9/2/2026, 12:16:46 PM
1class Solution:
2    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
3        remainder = {0: -1}
4        total = 0
5
6        for i, num in enumerate(nums):
7            total += num
8            rem = total % k
9
10            if rem in remainder:
11                if i - remainder[rem] >= 2:
12                    return True
13            else:
14                remainder[rem] = i
15
16        return False