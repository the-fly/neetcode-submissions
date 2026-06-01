class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 0:
            return -1
        if size == 1 and target == nums[0]:
            return 0
        
        mid = int(size/2)-1

        if (nums[mid] > target):
            return self.binarySearch(nums, target, 0, mid)
        else:
            return self.binarySearch(nums, target, mid, size)


    def binarySearch(self, nums: List[int], target: int, i: int, j: int) -> int:
        size = j-i
        if size == 0:
            return -1

        if size <= 3:
            for index in range(i,j):
                if nums[index] == target:
                    return index
            return -1
        if size == 1 and target == nums[i]:
            return i

        midIndex = i + int(size/2) -1

        if nums[midIndex] > target:
            return self.binarySearch(nums, target, i, midIndex)
        elif nums[midIndex] == target:
            return midIndex
        else:
            return self.binarySearch(nums, target, midIndex + 1, j)





