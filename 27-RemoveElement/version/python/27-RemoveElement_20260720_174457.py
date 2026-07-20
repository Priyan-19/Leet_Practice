# Last updated: 7/20/2026, 5:44:57 PM
1class Solution:
2    def sortedSquares(self, nums: List[int]) -> List[int]:
3        l=0
4        r=len(nums)-1
5
6        while(l<=r):
7            if nums[l]**2 < nums[r]**2:
8                nums[r],nums[l]=nums[r]**2,nums[l]**2
9                l+=1
10                r-=1
11            else:
12                nums[l],nums[r]=nums[l]**2,nums[r]**2
13                l+=1
14                r-=1
15        return sorted(nums)