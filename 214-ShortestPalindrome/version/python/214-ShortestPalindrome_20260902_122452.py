# Last updated: 9/2/2026, 12:24:52 PM
1class Solution:
2    def shortestPalindrome(self, s: str) -> str:
3        rev = s[::-1]
4
5        for i in range(len(s)):
6            if s[:len(s) - i] == rev[i:]:
7                return rev[:i] + s
8
9        return ""