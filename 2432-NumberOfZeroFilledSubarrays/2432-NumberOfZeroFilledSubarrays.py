# Last updated: 7/14/2026, 11:57:28 AM
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        run=0
        count=0
        for num in nums:
            if num==0:
                run+=1
            else :
                run = 0
            count=count+run
        return count
        