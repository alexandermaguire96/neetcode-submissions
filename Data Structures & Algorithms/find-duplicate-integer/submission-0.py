class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        easy = sorted(nums)

        for n in range(len(easy)):
            print(n, n+1)
            if easy[n] == easy[n + 1]:
                return easy[n]

        return n