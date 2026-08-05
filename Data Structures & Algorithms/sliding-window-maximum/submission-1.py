class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        heap = []
        n = len(nums)
        
        for i in range(0, k):
            heapq.heappush(heap, (-nums[i], i))

        res.append(-heap[0][0])
        # print(heap, "original window")
        # print(res, "original res")
        # print("--------now for the rest of the nums--------")

        for i in range(k, len(nums)):

            heapq.heappush(heap, (-nums[i], i)) 
            # print(heap, "new push",  "num[i]", -nums[i],",", i, "i") 

            # print(heap[0][1], "heap[0][1]", "i - k", i, "-" ,k, "=", i - k)
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            res.append(-heap[0][0])
            # print(res, "res")

        
        return res