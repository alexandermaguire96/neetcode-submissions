import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        Points = []

        for point in points:

            z = math.sqrt(point[0]**2 + point[1]**2)
            tuplePoints = (-z, point[0], point[1])
            Points.append(tuplePoints)
            
        heapq.heapify(Points)

        while len(Points) > k:
            heapq.heappop(Points)

        result = [(x,y) for (_, x, y) in Points]
        return result