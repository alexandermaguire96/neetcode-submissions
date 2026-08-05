class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashmap = Counter(nums)
        longest = 0

        for key in hashmap:
            length = 1
            if (key - 1) not in hashmap:
                while key + length in hashmap:
                    length += 1

                longest = max(length, longest)

        return longest

