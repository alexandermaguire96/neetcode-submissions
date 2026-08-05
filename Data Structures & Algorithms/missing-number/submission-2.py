class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        

        count = 0

        for num in sorted(nums):

            if num != count:
                return count

            count += 1

        return count