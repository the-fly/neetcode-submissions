class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=3:
            return max(nums)

        # Case1 0 and n not included
        prev = nums[1]
        curr = max(nums[1], nums[2])
        res = 0

        for i in range(3,n-1):
            prev, curr = max(prev,curr), max(prev + nums[i], curr - nums[i-1] + nums[i])
        
        res = max(res,curr, prev)

        prev = nums[1]
        curr = max(nums[1], nums[2])
        for i in range(3,n):
            prev, curr = max(prev,curr), max(prev + nums[i], curr - nums[i-1] + nums[i])
        res = max(res,curr, prev)

        prev = nums[0]
        curr = max(nums[0], nums[1])
        for i in range(2,n-1):
            prev, curr = max(prev,curr), max(prev + nums[i], curr - nums[i-1] + nums[i])
        res = max(res,curr, prev)
        return res
        

        