class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hashm:
                return [hashm[diff], i]
            else:
                hashm[v] = i
        return