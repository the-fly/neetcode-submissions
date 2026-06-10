class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minPointHeap = [(-self.eucledianDist(point), point) for point in points[0:k]]
        heapq.heapify(minPointHeap)
        for point in points[k:]:
            dist = -self.eucledianDist((point))
            if dist > minPointHeap[0][0]:
                heapq.heappush(minPointHeap, (dist, point))
                heapq.heappop(minPointHeap)

        return [point for (dist,point) in minPointHeap]

    def eucledianDist(self, point: (int, int)):
        return point[0]* point[0] + point[1]* point[1]
        