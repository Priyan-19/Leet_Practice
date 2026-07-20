# Last updated: 7/20/2026, 11:59:30 AM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l=0
4        r=len(numbers)-1
5        while(l<r):
6            ac=numbers[l]+numbers[r]
7            if ac>target:
8                r-=1
9            elif ac<target:
10                l+=1
11            else :
12                return [l+1,r+1]
13        