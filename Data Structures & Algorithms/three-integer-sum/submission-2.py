class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resSet = set()

        for middle in range(1, len(nums) - 1):
            left, right = 0, len(nums) - 1
            while (left < middle and middle <right):
                currSum = nums[left] + nums[middle] + nums[right]
                if currSum == 0:
                    resSet.add((nums[left], nums[middle], nums[right]))
                    left += 1
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    right -= 1
        res = [list(t) for t in resSet]

        return res
        