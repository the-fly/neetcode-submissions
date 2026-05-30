class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count0 = 0
        res = []
        for num in nums:
            if num == 0:
                count0 += 1
        if count0 >= 2:
            for i in range(0,len(nums)):
                res.append(0)
            return res
        if count0 == 1:
            product = 1
            index0 = 0
            for i in range(0,len(nums)):
                if not nums[i] == 0:
                    res.insert(i, 0)
                    product = product*nums[i]
                else:
                    index0 = i
            res.insert(index0, product)
            return res

        for num in nums:
            product *= num
        for num in nums:
            res.append(product // num)
        return res
        