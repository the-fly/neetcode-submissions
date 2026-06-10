class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minPointHeap = [(self.eucledianDist(point), point) for point in points]
        # heapq.heapify(minPointHeap)
        return [distAndPoint[1] for distAndPoint in heapq.nsmallest(k, minPointHeap)]


        # return heapq.nsmallest(k, minPointHeap)

    def eucledianDist(self, point: (int, int)):
        return point[0]* point[0] + point[1]* point[1]
        