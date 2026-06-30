class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        LISArray = [1 for _ in nums]
        res = 0

        for index in range(len(nums)):
            height = nums[index]
            j = index
            prevMax = 0
            for j in reversed(range(index)):
                if nums[j] < height:
                    prevMax = max(prevMax, LISArray[j])
            LISArray[index] = 1 + prevMax
            # res = max(res, LISArray[index])
        return max(LISArray)



        