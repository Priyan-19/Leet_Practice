# Last updated: 9/2/2026, 12:14:03 PM
1class Solution:
2    def maximumGap(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        if n < 2:
6            return 0
7
8        mn = min(nums)
9        mx = max(nums)
10
11        if mn == mx:
12            return 0
13
14        bucket_size = max(1, (mx - mn) // (n - 1))
15        bucket_count = (mx - mn) // bucket_size + 1
16
17        buckets = [[float('inf'), float('-inf')]
18                   for _ in range(bucket_count)]
19
20        for num in nums:
21            index = (num - mn) // bucket_size
22
23            buckets[index][0] = min(buckets[index][0], num)
24            buckets[index][1] = max(buckets[index][1], num)
25
26        answer = 0
27        previous_max = mn
28
29        for bucket_min, bucket_max in buckets:
30            if bucket_min == float('inf'):
31                continue
32
33            answer = max(answer, bucket_min - previous_max)
34            previous_max = bucket_max
35
36        return answer