class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        
        res = -1001
        for j in range(0, len(nums)):    
            
            total = 0
            for i in range(j, len(nums)):

                total += nums[i]
                res = max(total, res)

        return res