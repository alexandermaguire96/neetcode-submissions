class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0] * (len(cost))

        #baseline
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(len(dp)):

            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        
        return min(dp[-1], dp[-2])
        
