class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 0
        best = 0
        
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                good = prices[sell] - prices[buy]
                best = max(best, good)
            else:
                buy = sell
            sell += 1

        return best
