import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x,y = points[i]
            dist = x**2+y**2
            heapq.heappush(heap,(-dist,(x,y)))
            if len(heap)>k:
                heapq.heappop(heap)
        return [point for val,point in heap]
        