class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums)-1)


    def binarySearch(self, nums: List[int], target: int, i: int, j: int) -> int:
        print(i,j)
        if i>j:
            return -1

        if j-i <= 1:
            if nums[i] == target:
                return i
            if j == i+1 and nums[j] == target:
                return j
            return -1
        
        mid = i + (j-i) // 2

        middle = nums[mid]

        if middle == target:
            return mid
        
        left = nums[i]
        right = nums[j]
        
        if ((middle > left and middle > target and left <= target) or (middle < left and (target < middle or target >=left))):
            return self.binarySearch(nums, target, i, mid-1)
        return self.binarySearch(nums, target, mid+1, j)

