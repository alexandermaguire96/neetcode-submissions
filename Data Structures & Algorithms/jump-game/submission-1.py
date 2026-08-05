class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        memo = {}

        def jump(i):

            if i >= len(nums)-1:
                return True

            if i in memo:
                return memo[i]

            for path in range(i + 1, i + nums[i] + 1):
                if jump(path):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return jump(0)

