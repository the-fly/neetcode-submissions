class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        maxHeight = piles[-1]

        return self.binaryBiteSize(piles, h, 1, maxHeight)
    
    def binaryBiteSize(self, piles: List[int], target: int, left, right) -> int:

        print(left,right)
        if right < left:
            return -1
        mid = left + (right - left) // 2

        hoursRequired = 0

        for height in piles:
            hoursRequired += height // mid
            if not height % mid == 0:
                hoursRequired += 1
            
        if hoursRequired <= target:
            if mid-left >= 1:
                return  self.binaryBiteSize(piles, target, left, mid)
            else:
                return mid
        else:
            return  self.binaryBiteSize(piles, target, mid+1, right)

        