class MedianFinder:

    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftMaxHeap, -num)

        if (len(self.leftMaxHeap) - len(self.rightMinHeap)) > 1:
            # print('a', num, len(self.leftMaxHeap), len(self.rightMinHeap))
            leftMax = -heapq.heappop(self.leftMaxHeap)
            heapq.heappush(self.rightMinHeap, leftMax)
        
        if (len(self.leftMaxHeap)>0 and len(self.rightMinHeap)>0 and -self.leftMaxHeap[0]>self.rightMinHeap[0]):
            leftMax = -heapq.heappop(self.leftMaxHeap)
            rightMin = heapq.heappop(self.rightMinHeap)
            heapq.heappush(self.rightMinHeap, leftMax)
            heapq.heappush(self.leftMaxHeap, -rightMin)

    def findMedian(self) -> float:
        # print('b', self.leftMaxHeap, self.rightMinHeap)
        if (len(self.leftMaxHeap) - len(self.rightMinHeap)) == 1:
            return -self.leftMaxHeap[0]
        else:
            return (-self.leftMaxHeap[0]+self.rightMinHeap[0])/2
        
        