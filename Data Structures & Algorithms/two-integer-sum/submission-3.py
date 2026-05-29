class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unsortedNums = nums.copy()
        nums.sort()
        i, j = 0, len(nums) - 1
        while (i<j):
            sumij = nums[i]+nums[j]
            if sumij == target:
                break
            elif sumij < target:
                i += 1
            elif sumij > target:
                j -= 1
        originalIndexI, originalIndexJ = -1,-1
        print(unsortedNums)
        for index in range(0, len(unsortedNums)):
            
            if unsortedNums[index] == nums[i] or unsortedNums[index] == nums[j]:
                if originalIndexI<0:
                    originalIndexI = index
                else:
                    originalIndexJ = index
        return [originalIndexI, originalIndexJ]
        