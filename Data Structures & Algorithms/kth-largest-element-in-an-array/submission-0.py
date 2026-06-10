class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        print (nums)
        return -heapq.nsmallest(k, nums)[k-1]

        