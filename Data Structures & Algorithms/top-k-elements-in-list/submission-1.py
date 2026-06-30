import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []

        for n in nums : 
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items() :
            heapq.heappush(heap, (c, n))

            if len(heap) > k :
                heapq.heappop(heap)
        return [n for c, n in heap]