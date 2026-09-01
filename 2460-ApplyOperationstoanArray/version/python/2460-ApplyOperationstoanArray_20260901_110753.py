# Last updated: 9/1/2026, 11:07:53 AM
1class Solution:
2    def applyOperations(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        for i in range(n-1):
5            if nums[i]==nums[i+1]:
6                nums[i]*=2
7                nums[i+1]=0
8            
9        k=0
10        for i in range(n):
11            if nums[i]!=0:
12                nums[k]=nums[i]
13                k+=1
14
15        for i in range(k,n):
16            nums[i]=0
17
18        return nums
19