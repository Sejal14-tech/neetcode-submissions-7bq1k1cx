#heap solution is needed here
from heapq import heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        dicts = {}
        for i in nums:
            dicts[i] = dicts.get(i,0)+1
        for key,value in dicts.items():
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for count,num in heap]
        



        