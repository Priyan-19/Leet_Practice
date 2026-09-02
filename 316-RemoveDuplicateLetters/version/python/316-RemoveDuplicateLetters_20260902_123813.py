# Last updated: 9/2/2026, 12:38:13 PM
1from collections import Counter
2
3class Solution:
4    def removeDuplicateLetters(self, s: str) -> str:
5        count = Counter(s)
6        stack = []
7        seen = set()
8
9        for char in s:
10            count[char] -= 1
11
12            if char in seen:
13                continue
14
15            while stack and char < stack[-1] and count[stack[-1]] > 0:
16                removed = stack.pop()
17                seen.remove(removed)
18
19            stack.append(char)
20            seen.add(char)
21
22        return ''.join(stack)