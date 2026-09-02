# Last updated: 9/2/2026, 1:35:54 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        if not digits:
4            return []
5
6        phone = {
7            '2': 'abc',
8            '3': 'def',
9            '4': 'ghi',
10            '5': 'jkl',
11            '6': 'mno',
12            '7': 'pqrs',
13            '8': 'tuv',
14            '9': 'wxyz'
15        }
16
17        result = []
18
19        def backtrack(index, current):
20            if index == len(digits):
21                result.append(current)
22                return
23
24            letters = phone[digits[index]]
25
26            for char in letters:
27                backtrack(index + 1, current + char)
28
29        backtrack(0, "")
30
31        return result