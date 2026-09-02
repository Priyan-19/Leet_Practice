# Last updated: 9/2/2026, 12:29:55 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        i = m - 1
4        j = n - 1
5        k = m + n - 1
6
7        while j >= 0:
8            if i >= 0 and nums1[i] > nums2[j]:
9                nums1[k] = nums1[i]
10                i -= 1
11            else:
12                nums1[k] = nums2[j]
13                j -= 1
14
15            k -= 1