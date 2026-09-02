# Last updated: 9/2/2026, 1:44:22 PM
1class Solution:
2    def sortArrayByParity(self, nums: List[int]) -> List[int]:
3        even = []
4        odd = []
5
6        for num in nums:
7            if num % 2 == 0:
8                even.append(num)
9            else:
10                odd.append(num)
11
12        return even + odd