# Last updated: 9/2/2026, 12:47:54 PM
1from typing import List
2
3class Solution:
4    def minSideJumps(self, obstacles: List[int]) -> int:
5        dp = [1, 0, 1]  # lane1, lane2, lane3
6
7        for obstacle in obstacles:
8            if obstacle:
9                dp[obstacle - 1] = float('inf')
10
11            for lane in range(3):
12                if lane != obstacle - 1:
13                    dp[lane] = min(dp[lane], min(dp[(lane+1)%3], dp[(lane+2)%3]) + 1)
14
15        return min(dp)
16