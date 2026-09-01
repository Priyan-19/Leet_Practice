# Last updated: 9/1/2026, 11:36:23 PM
1class Solution:
2        def countOperationsToEmptyArray(self, A: List[int]) -> int:
3            pos = {a: i for i, a in enumerate(A)}
4            res = n = len(A)
5            A.sort()
6            for i in range(1, n):
7                if pos[A[i]] < pos[A[i - 1]]:
8                    res += n - i
9            return res