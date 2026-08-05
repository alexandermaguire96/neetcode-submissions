class Solution:
    def rob(self, nums: List[int]) -> int:
       
        dp = [0] * len(nums)

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max((nums[2] + dp[0]), dp[1])

        for i in range(3,len(nums),1):
            dp[i] = max(nums[i] + dp[i-2], nums[i] + dp[i-3])

        

        return max(dp[-1], dp[-2])