# Last updated: 9/2/2026, 2:00:55 PM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        n = len(needle)
4
5        for i in range(len(haystack) - n + 1):
6            if haystack[i:i + n] == needle:
7                return i
8
9        return -1