# Last updated: 9/2/2026, 9:43:07 AM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        from functools import lru_cache
4
5        @lru_cache(None)
6        def dp(i, j):
7            # if one string empty → need to insert/delete all chars
8            if i == len(word1): return len(word2) - j
9            if j == len(word2): return len(word1) - i
10
11            if word1[i] == word2[j]:
12                return dp(i+1, j+1)  # no operation
13            else:
14                return 1 + min(
15                    dp(i+1, j),    # delete
16                    dp(i, j+1),    # insert
17                    dp(i+1, j+1)   # replace
18                )
19
20        return dp(0, 0)
21