class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        nums_sum = sum(nums)

        if nums_sum % 2 != 0:
            return False
        
        half_sum = nums_sum // 2
        print("half_sum made!")

        dp = [False] * (half_sum + 1)
        dp[0] = True

        for i in range(n):
            for j in range(half_sum, nums[i]-1, -1):
                target = j - nums[i]
                if dp[target]:
                    dp[j] = True
                    
                


                print(dp, "i = ", i, "n[i] = ", nums[i], "j = ", j)


        return dp[half_sum]
        
