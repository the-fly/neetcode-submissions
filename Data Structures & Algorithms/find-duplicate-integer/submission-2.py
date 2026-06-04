# Usaing Hash
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            if num in numSet:
                return num
            else: numSet.add(num)
        return 0
        