# Last updated: 7/24/2026, 11:03:28 AM
1class Solution:
2    def searchInsert(self, arr: List[int], t: int) -> int:
3        for i in range(0,len(arr)):
4            if arr[i]>=t:
5                return i
6        return len(arr)
7
8        