class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        
        
        if not nums:
            return 0

        if n == 1:
            return nums[0]

        dp_max = nums[0]
        dp_min = nums[0]
        res = nums[0]
        
        for i in range(1, n):
            if nums[i] < 0:
                    dp_max, dp_min = dp_min, dp_max

            dp_max = max(dp_max * nums[i], nums[i])
            dp_min = min(dp_min * nums[i], nums[i])

            res = max(res, dp_max)

        return res