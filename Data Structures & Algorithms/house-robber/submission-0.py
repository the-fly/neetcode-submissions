class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <2 :
            return min(nums)
        
        prev = nums[0]
        curr = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            prev, curr = max(prev,curr), max(prev + nums[i], curr-nums[i-1] + nums[i])

        return max(prev, curr)
        

        