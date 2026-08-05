class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                cur_length = 1
                while num + 1 in nums_set:
                    cur_length += 1
                    num += 1
                   
                longest = max(cur_length, longest)
                    
        return longest
            
