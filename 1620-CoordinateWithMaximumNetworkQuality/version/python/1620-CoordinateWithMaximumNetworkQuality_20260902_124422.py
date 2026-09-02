# Last updated: 9/2/2026, 12:44:22 PM
1class Solution:
2    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
3        best = [0, 0]
4        max_quality = 0
5
6        for x in range(51):
7            for y in range(51):
8                quality = 0
9
10                for tx, ty, q in towers:
11                    distance = ((x - tx) ** 2 + (y - ty) ** 2) ** 0.5
12
13                    if distance <= radius:
14                        quality += int(q / (1 + distance))
15
16                if quality > max_quality:
17                    max_quality = quality
18                    best = [x, y]
19
20        return best