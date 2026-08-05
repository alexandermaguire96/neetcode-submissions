class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else: hi = mid

        pivot = lo
        
        if nums[pivot] <= target <= nums[-1]:
            l, r = pivot, len(nums)-1
        else:
            l, r = 0, pivot - 1

        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else: r = m - 1

        return -1
        #FIRST STRATEGY, TOO COMPLICATED
        # if target == nums[pivot]:
        #     return pivot
        # elif target <= nums[pivot-1]:
        #     l, r = 0, pivot - 1
        #     while l <= r:
        #         m = l + (r-l)//2
        #         if target == nums[m]:
        #             return m
        #         elif nums[m] > nums[r]:
        #             l = m + 1
        #         else: r = m - 1
            
        
        # elif target > nums[pivot]:
        #     l, r = pivot + 1, len(nums) -1
        #     while l <= r:
        #         m = l + (r-l)//2
        #         if nums[m] == target:
        #             return m
        #         if nums[m] > nums[r]:
        #             l = m + 1
        #         else: r = m - 1
            
                
        