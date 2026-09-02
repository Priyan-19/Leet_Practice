# Last updated: 9/2/2026, 1:45:19 PM
1class Solution:
2    def sortEvenOdd(self, nums: List[int]) -> List[int]:
3        even = nums[::2]
4        odd = nums[1::2]
5
6        even.sort()
7        odd.sort(reverse=True)
8
9        nums[::2] = even
10        nums[1::2] = odd
11
12        return nums