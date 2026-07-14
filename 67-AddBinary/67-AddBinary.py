# Last updated: 7/14/2026, 11:58:20 AM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x= bin((int(a,2))+(int(b,2)))
        return x[2:]
