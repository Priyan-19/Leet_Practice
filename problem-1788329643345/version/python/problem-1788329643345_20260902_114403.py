# Last updated: 9/2/2026, 11:44:03 AM
1class Solution:
2    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
3        i = len(num) - 1
4
5        while i >= 0 or k > 0:
6            if i >= 0:
7                k += num[i]
8                num[i] = k % 10
9                k //= 10
10                i -= 1
11            else:
12                num.insert(0, k % 10)
13                k //= 10
14
15        return num