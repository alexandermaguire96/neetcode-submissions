class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_Buy = prices[0]

        for sell in prices:
            max_profit = max(max_profit, sell - min_Buy)
            min_Buy = min(min_Buy, sell)
        return max_profit