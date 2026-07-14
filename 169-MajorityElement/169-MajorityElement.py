# Last updated: 7/14/2026, 11:58:04 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(count.keys(), key=count.get)