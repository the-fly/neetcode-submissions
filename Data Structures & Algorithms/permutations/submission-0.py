class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [[nums[0]]]
        for i in range(len(nums)):
            permutations = self.permute(nums[:i] + nums[i+1:])
            for perm in permutations:
                perm.append(nums[i])
                res.append(perm)
            
        return res


    # def permutate(self, nums: List[int]):
            
        