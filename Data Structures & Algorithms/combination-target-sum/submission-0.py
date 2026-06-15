class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        curr = []
        currSum = 0

        def dfs(i):
            nonlocal currSum
            if currSum == target:
                res.append(curr[:])
                return

            if i >= len(nums) or currSum > target:
                return
            
            # case: adding num i
            currSum += nums[i]
            curr.append(nums[i])
            dfs(i)

            currSum -= nums[i]
            curr.pop()
            dfs(i+1)
        
        dfs(0)
        return res
            


        