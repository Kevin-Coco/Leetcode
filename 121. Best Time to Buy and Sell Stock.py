# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        max_profit = 0
        cur_min = prices[0]
        
        for i in range(1, len(prices)):
            if cur_min < prices[i]:
                max_profit = max(max_profit, prices[i] - cur_min)
            else:
                cur_min = prices[i]
        
        return max_profit
