# Last updated: 9/2/2026, 9:35:59 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        char_index = {}   
4        left = 0
5        max_len = 0
6
7        for right in range(len(s)):
8            if s[right] in char_index and char_index[s[right]] >= left:
9                left = char_index[s[right]] + 1
10            char_index[s[right]] = right
11            max_len = max(max_len, right - left + 1)
12
13        return max_len
14