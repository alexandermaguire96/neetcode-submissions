class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        seen = []
        def helper(nums, path, seen, index):
            #base case
            if index >= len(nums):
                seen.append(path)
                return


            #recursive statement
            
            helper(nums, path + [nums[index]], seen, index + 1)
            helper(nums, path, seen, index + 1)

            #return
            return
        helper(nums, [], seen, 0)
        return seen
        