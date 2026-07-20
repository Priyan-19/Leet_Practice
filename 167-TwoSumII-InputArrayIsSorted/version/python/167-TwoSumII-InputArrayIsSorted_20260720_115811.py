# Last updated: 7/20/2026, 11:58:11 AM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l=0
4        r=len(numbers)-1
5        li=[]
6        while(l<r):
7            ac=numbers[l]+numbers[r]
8            if ac>target:
9                r-=1
10            elif ac<target:
11                l+=1
12            else :
13                li.append(l+1)
14                li.append(r+1)
15                l+=1
16                r-=1
17        return li
18        