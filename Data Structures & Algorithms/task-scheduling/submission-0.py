import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        taskList = [0] * 26

        for task in tasks:
            key = ord(task) - ord('A')
            taskList[key] += 1

        
        maxHeap = [-task for task in taskList if task > 0]
        heapq.heapify(maxHeap)

        time = 0
        while maxHeap:
            sequence = []
            intervals = 0
            for _ in range(n+1):
                if maxHeap:
                    freq = -heapq.heappop(maxHeap)
                    if freq - 1 > 0:
                        sequence.append(freq - 1)
                    intervals += 1

            for freq in sequence:
                heapq.heappush(maxHeap, -freq)

            time += intervals if not maxHeap else n + 1

        return time





        