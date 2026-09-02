# Last updated: 9/2/2026, 1:42:44 PM
1class Solution:
2    def rearrangeArray(self, nums: List[int]) -> List[int]:
3        positive = []
4        negative = []
5
6        for num in nums:
7            if num > 0:
8                positive.append(num)
9            else:
10                negative.append(num)
11
12        result = []
13
14        for i in range(len(positive)):
15            result.append(positive[i])
16            result.append(negative[i])
17
18        return result