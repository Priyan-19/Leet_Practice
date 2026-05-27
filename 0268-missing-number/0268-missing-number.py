class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        su = n*(n+1)//2
        asum =0
        for i in nums:
            asum+=i
        return su-asum
