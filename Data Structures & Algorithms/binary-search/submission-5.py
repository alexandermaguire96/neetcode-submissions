class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lo, hi = 0, len(nums)

        if target > max(nums):
            return -1
        if target < min(nums):
            return -1

        for num in nums:
            mid = lo + hi // 2
            if nums[mid] < target:
                lo += 1
            if nums[mid] > target:
                hi -= 1
            
            if nums[mid] == target:
                return mid
        return -1