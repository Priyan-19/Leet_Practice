# Last updated: 9/2/2026, 11:15:44 AM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3
4        slow = nums[0]
5        fast = nums[0]
6
7        while True:
8            slow = nums[slow]
9            fast = nums[nums[fast]]
10
11            if slow == fast:
12                break
13
14
15        slow = nums[0]
16
17        while slow != fast:
18            slow = nums[slow]
19            fast = nums[fast]
20
21        return slow