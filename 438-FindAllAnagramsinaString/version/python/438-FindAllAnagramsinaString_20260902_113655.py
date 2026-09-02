# Last updated: 9/2/2026, 11:36:55 AM
1from collections import Counter
2
3class Solution:
4    def findAnagrams(self, s: str, p: str) -> List[int]:
5        result = []
6
7        p_count = Counter(p)
8        window_count = Counter()
9
10        left = 0
11
12        for right in range(len(s)):
13            window_count[s[right]] += 1
14
15            # Keep window size equal to len(p)
16            if right - left + 1 > len(p):
17                window_count[s[left]] -= 1
18
19                if window_count[s[left]] == 0:
20                    del window_count[s[left]]
21
22                left += 1
23
24            # Check anagram
25            if window_count == p_count:
26                result.append(left)
27
28        return result