class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s=input()
        s=s.strip()
        s=s.split()
        return(len(s[-1]))