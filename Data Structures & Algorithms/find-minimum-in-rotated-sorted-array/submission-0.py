class Solution:
    def findMin(self, nums: List[int]) -> int:

        return self.rotatedBinarySearch(nums, 0, len(nums)-1)


    def rotatedBinarySearch(self, nums: List[int], i: int, j: int):

        if i == j:
            return nums[i]

        left = nums[i]
        right = nums[j]
        if j == i+1:
            return min(nums[i], nums[j])

        p = i + (j-i) // 2
        mid = nums[p]

        if mid < left:
            return self.rotatedBinarySearch(nums, i, p)

        if left < right:
            return left

        return self.rotatedBinarySearch(nums, p+1, j)
        

        