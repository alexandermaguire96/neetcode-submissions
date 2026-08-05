class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * n

        #baseline
        dp[0] = 1
        if len(dp) > 1:
            dp[1] = 2

        for i in range(2,len(dp),1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[-1]
