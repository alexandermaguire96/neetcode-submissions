class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        working = [nums[x] for x in range(len(nums))]
        check = set()

        def helper(path, working, check):
            
            copy = path.copy()
            
            if tuple(sorted(copy)) not in check:
                res.append(copy)
                check.add(tuple(sorted(copy)))

            if len(path) == len(nums):
                return

            
            for i in range(len(working)):
                save = working.copy()
                path.append(working[i])
                working.pop(i)
                helper(path, working, check)
                path.pop()
                working = save

            

        helper([], working, check)
        return res