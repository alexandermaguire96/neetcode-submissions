class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #heapq.nlargest gives the largest numbers
        #heapq.nsmallest gives the smallest numbers
        new_nums = heapq.nlargest(k, nums)
        return heapq.nsmallest(1, new_nums)[0]
        
        