class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

            num_map = {}

            for i, num in enumerate(nums):
                j = target - num

                if j in num_map:
                    return [num_map[j], i]

                num_map[num] = i

            return []