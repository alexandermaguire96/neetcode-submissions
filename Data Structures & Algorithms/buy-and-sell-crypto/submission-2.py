class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 0
        best_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                best_profit = max(profit, best_profit)
            else:
                l = r
            r += 1

        return best_profit

