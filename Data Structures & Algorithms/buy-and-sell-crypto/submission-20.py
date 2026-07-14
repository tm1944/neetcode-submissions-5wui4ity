class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                res = max(profit,res)
            else:
                l=r
            r+=1
        return res