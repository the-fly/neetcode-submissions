class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Consider a graph with y = sum(nums[0:x])
        # Maximum subarray will be the longest upward movement of this graph
        # That is the difference between maxima and minima where minima is on the left of maxima
        minima, maxima = 0, 0
        res = max(nums)

        summation = 0
        for num in nums:
            summation += num
            if summation < minima:
                minima = summation
                maxima = summation
            elif summation > maxima:
                maxima = summation
                res = max(res, maxima - minima)
        return res
