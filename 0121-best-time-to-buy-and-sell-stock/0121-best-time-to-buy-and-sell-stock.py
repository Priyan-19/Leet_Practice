class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        max=0
        for i in range(len(prices)):
            if prices[i]<min:
                min=prices[i]
            else:
                p=prices[i]-min
                if p>max:
                    max =p
        return max

        