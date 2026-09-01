# Last updated: 9/1/2026, 11:41:54 PM
1from typing import List
2
3class Solution:
4    def maxArea(self, height: List[int]) -> int:
5        left, right = 0, len(height) - 1
6        max_area = 0
7
8        while left < right:
9            width = right - left
10            h = min(height[left], height[right])
11            max_area = max(max_area, width * h)
12
13            if height[left] < height[right]:
14                left += 1
15            else:
16                right -= 1
17
18        return max_area
19