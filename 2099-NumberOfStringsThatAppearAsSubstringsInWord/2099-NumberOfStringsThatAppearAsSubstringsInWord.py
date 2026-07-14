# Last updated: 7/14/2026, 11:57:32 AM
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c=0
        for i in patterns:
            if i in word:
                c+=1

                
        return c