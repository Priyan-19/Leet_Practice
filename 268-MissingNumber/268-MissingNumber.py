# Last updated: 7/14/2026, 11:57:54 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        ex=n*(n+1)//2
        ax=sum(nums)
        return ex-ax