# Last updated: 7/14/2026, 11:58:22 AM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        val = "".join(str(i) for i in digits)
        val = str(int(val)+1)
        digit =[int(i) for i in val]
        return (digit)
