class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        currSubset = []

        def dfs(i):
            if i == len(nums):
                res.append(currSubset[:])
                return
            
            currSubset.append(nums[i])
            dfs(i+1)
            currSubset.pop()

            j = i+1
            while j<len(nums) and nums[j]==nums[i]:
                j = j+1
            dfs(j)
        
        dfs(0)
        return res