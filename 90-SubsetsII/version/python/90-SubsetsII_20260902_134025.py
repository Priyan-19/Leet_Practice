# Last updated: 9/2/2026, 1:40:25 PM
1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        result = []
5
6        def backtrack(start, current):
7            result.append(current[:])
8
9            for i in range(start, len(nums)):
10
11                # Skip duplicate choices at the same level
12                if i > start and nums[i] == nums[i - 1]:
13                    continue
14
15                current.append(nums[i])
16                backtrack(i + 1, current)
17                current.pop()
18
19        backtrack(0, [])
20
21        return result