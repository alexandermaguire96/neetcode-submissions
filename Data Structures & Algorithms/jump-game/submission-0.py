class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        def jump(nums, i):

            if i >= len(nums)-1:
                return True

            for path in range(i + 1, i + nums[i] + 1):
                if jump(nums, path):
                    return True

            return False

        return jump(nums, 0)

