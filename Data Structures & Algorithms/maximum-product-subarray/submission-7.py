class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0] * n
        dp_min = [0] * n
        
        if not nums:
            return 0

        if n == 1:
            return nums[0]


        dp[0] = nums[0]
        dp_min[0] = nums[0]
        
        dp[1] = max(nums[0] * nums[1], nums[1])
        dp_min[1] = min(nums[0]* nums[1], nums[1])

        for i in range(2,n):
            if nums[i] <= 0:
                    dp[i] = max(dp_min[i-1]* nums[i], nums[i], dp[i-1] * nums[i])
                    dp_min[i] = min(dp_min[i-1] * nums[i], nums[i], dp[i-1] * nums[i])
            elif nums[i] > 0:
                dp[i] = max(dp[i-1]*nums[i], nums[i])
                dp_min[i] = min(dp_min[i-1]*nums[i], nums[i])

        return max(dp)