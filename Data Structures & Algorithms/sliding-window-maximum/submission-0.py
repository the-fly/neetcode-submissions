class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windowMax, maxIndex = nums[0], 0
        res = []

        for i in range(k):
            if nums[i] >= windowMax:
                windowMax = nums[i]
                maxIndex = i

        res.append(windowMax)
        if (k == len(nums)):
            return res

        for i in range(k,len(nums)):
            if nums[i] >= windowMax:
                windowMax = nums[i];
                maxIndex = i
                res.append(windowMax)
            elif nums[i-k] == windowMax:
                windowMax = nums[i-k+1]
                maxIndex = i-k+1
                for j in range(i-k+1,i+1):
                    if nums[j] >= windowMax:
                        windowMax = nums[j]
                        maxIndex = j
                res.append(windowMax)
            else:
                res.append(windowMax)

        return res
            

        