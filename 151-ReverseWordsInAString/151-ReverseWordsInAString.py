# Last updated: 7/14/2026, 11:58:12 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        s= s.split()
        s=" ".join(s[::-1])
        return s