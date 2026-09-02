# Last updated: 9/2/2026, 11:36:12 AM
1from collections import Counter
2
3class Solution:
4    def isAnagram(self, s: str, t: str) -> bool:
5        return Counter(s) == Counter(t)