class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minima, maxima = 0, 0
        res = max(nums)

        summation = 0
        numsS = []
        for num in nums:
            summation += num
            if summation < minima:
                minima = summation
                maxima = summation
            elif summation > maxima:
                maxima = summation
                res = max(res, maxima - minima)
        return res


        
        