class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        elif len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        rob, rob2 = nums[0], max(nums[1], nums[0])

        for i in range(2, len(nums) -1, 1):
            dp1 = max(rob2, nums[i] + rob)
            rob = rob2
            rob2 = dp1
        
        [2,9,10,12]
        rob, rob2 = nums[1], max(nums[2], nums[1])
        for i in range(3,len(nums),1):
            dp2 = max(rob2, nums[i] + rob)
            rob = rob2
            rob2 = dp2

        

        return max(dp1, dp2) if dp1 else max()
        