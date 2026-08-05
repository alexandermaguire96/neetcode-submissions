class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        total = ((len(nums))*(len(nums) + 1)) // 2
        count = 0

        for num in nums:

            count += num


        return total - count
