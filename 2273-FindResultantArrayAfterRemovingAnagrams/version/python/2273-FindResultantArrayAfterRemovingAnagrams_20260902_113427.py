# Last updated: 9/2/2026, 11:34:27 AM
1class Solution:
2    def removeAnagrams(self, words: List[str]) -> List[str]:
3        result = []
4
5        for word in words:
6            if not result or sorted(word) != sorted(result[-1]):
7                result.append(word)
8
9        return result