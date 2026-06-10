class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        
        while(len(maxHeap)>1):
            bigStone = -heapq.heappop(maxHeap)
            lessBigStone = -heapq.heappop(maxHeap)
            if bigStone != lessBigStone:
                newStone = bigStone - lessBigStone
                heapq.heappush(maxHeap, -newStone)
        if len(maxHeap) == 1:
            return -heapq.heappop(maxHeap)
        
        return 0


        