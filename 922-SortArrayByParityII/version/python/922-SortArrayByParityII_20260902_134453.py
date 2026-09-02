# Last updated: 9/2/2026, 1:44:53 PM
1class Solution:
2    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
3        result = [0] * len(nums)
4
5        even = 0
6        odd = 1
7
8        for num in nums:
9            if num % 2 == 0:
10                result[even] = num
11                even += 2
12            else:
13                result[odd] = num
14                odd += 2
15
16        return result