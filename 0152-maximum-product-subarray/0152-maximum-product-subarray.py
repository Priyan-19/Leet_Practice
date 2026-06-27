class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = result = nums[0]
        
        for n in nums[1:]:
            temp = cur_max
            cur_max = max(n, n * cur_max, n * cur_min)
            cur_min = min(n, n * temp, n * cur_min)
            result = max(result, cur_max)
        
        return result