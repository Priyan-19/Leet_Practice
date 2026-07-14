# Last updated: 7/14/2026, 11:58:23 AM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s=input()
        s=s.strip()
        s=s.split()
        return(len(s[-1]))