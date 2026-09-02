# Last updated: 9/2/2026, 11:33:41 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        groups = {}
4
5        for word in strs:
6            key = ''.join(sorted(word))
7
8            if key not in groups:
9                groups[key] = []
10
11            groups[key].append(word)
12
13        return list(groups.values())