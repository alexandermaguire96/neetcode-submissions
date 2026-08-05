import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        #instantiate the heap and int k
        self.k = k
        self.heap = nums

        heapq.heapify(self.heap)

        #want heap to be k sized always
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        #if heap is smaller than k, just add to it
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        #if new val is larger than smallest node, add it and remove smallest
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)

        #return kth largest
        return self.heap[0]


        
