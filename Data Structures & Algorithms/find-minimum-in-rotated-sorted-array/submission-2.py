class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1

        while lo < hi:
            mid = lo + (hi-lo) // 2
            if nums[hi] > nums[lo]:
                return nums[lo]
            elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid + 1]:
                if nums[lo] > nums[lo+1]:
                    hi -= 1
                elif nums[hi] < nums[hi - 1]:
                    lo += 1
                else: lo += 1
            elif nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                return nums[mid] 
        return nums[0]

            