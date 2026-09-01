# Last updated: 9/1/2026, 11:39:20 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        prefixArray = [1]
4        for i in range(1,len(nums)):
5            prefixArray.append(prefixArray[-1]*nums[i-1])
6
7        suffixArray = [1]
8        for i in range(len(nums)-2, -1, -1):
9            suffixArray.append(suffixArray[-1]*nums[i+1])
10        suffixArray = suffixArray[::-1]
11        res = []
12        for i in range(len(nums)):
13            res.append(prefixArray[i]*suffixArray[i])
14        return res