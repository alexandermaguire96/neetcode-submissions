class Solution:
    def maxArea(self, heights: List[int]) -> int:
        end = len(heights)-1
        l, r = 0, end
        max_water = 0
        

        while l<r:
            cur_water = min(heights[l], heights[r]) * (r-l)
            max_water = max(cur_water, max_water)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
            print(cur_water)

        return max_water


