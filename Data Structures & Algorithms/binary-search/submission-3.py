class Solution:
    def search(self, nums: List[int], target: int) -> int:
        seen = set()

        for i, num in enumerate(nums):
            print(i, num)
            if num == target:
                return i
        return -1