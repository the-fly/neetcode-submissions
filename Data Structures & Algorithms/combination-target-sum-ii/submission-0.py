class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)
        res = []
        currNums = []
        currSum = 0
        
        def dfs(i):
            nonlocal currSum
            if currSum == target:
                res.append(currNums[:])
                return
            if i>=len(candidates) or currSum > target:
                return
            
            currSum += candidates[i]
            currNums.append(candidates[i])
            dfs(i+1)
            
            currSum -= candidates[i]
            currNums.pop()
            j= i+1
            while j< len(candidates) and candidates[i]==candidates[j]:
                j += 1
            dfs(j)
        
        dfs(0)

        return res

        