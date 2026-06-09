class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums[0:k], k
        heapq.heapify(self.minheap)

        for val in nums[k:]:
            if val>self.minheap[0]:
                heapq.heappop(self.minheap)
                heapq.heappush(self.minheap, val)

        

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
            
        elif val>self.minheap[0]:
            heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, val)

        return self.minheap[0]
        
