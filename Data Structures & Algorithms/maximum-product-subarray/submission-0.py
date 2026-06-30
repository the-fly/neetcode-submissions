class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) <2:
            return nums[0]
        nums.append(0)
        res = nums[0]
        preNegProduct = 1
        postNegProduct = 1
        currProduct = 1
        negCount = 0
        currLen = 0
        for num in nums:
            if num == 0:
                print(negCount, res, currProduct, preNegProduct, postNegProduct)
                if currLen == 0:
                    res = max(res,0)
                elif currLen == 1:
                    res = max(0, res, currProduct)
                elif negCount %2 == 0:
                    res = max(0, res, currProduct)
                else:
                    res = max(0, res, currProduct // preNegProduct, currProduct// postNegProduct)
                preNegProduct = 1
                postNegProduct = 1
                currProduct = 1
                negCount = 0
                currLen = 0
                continue
            currProduct *= num
            currLen += 1
            if num > 0:
                if negCount == 0 and num > 0:
                    preNegProduct *= num
                if negCount%2 == 1:
                    postNegProduct *= num
            
            if num<0:
                if negCount == 0:
                    preNegProduct *= num
                negCount += 1
                postNegProduct = num
        return res
    #     currSublist = []
    #     arrays = []
    #     for num in nums:
    #         if num == 0:
    #             if currSublist:
    #                 arrays.append(currSublist)
    #                 currSublist = []
    #         currSublist.append(num)
    #     if currSublist:
    #         arrays.append(currSublist)
        
    #     print (arrays)
    #     if not arrays:
    #         return 0

    #     res = nums[0]

    #     for array in arrays:
    #         res = max(res, self._findMaxProduct(array)) 
    #     return res  

    # def _findMaxProduct(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     firstNegIndex, lastNegIndex = -1, -1 
    #     negativeCount = 0
    #     for index in range(len(nums)):
    #         if nums[index] < 0:
    #             negativeCount += 1
    #             lastNegIndex = index
    #             if firstNegIndex == -1:
    #                 firstNegIndex = index
        
    #     print('n', negativeCount, nums)
    #     if negativeCount%2 == 0:
    #         return self._product(nums)
        
    #     if negativeCount == 1:
    #         return max(self._product(nums[:firstNegIndex]), self._product(nums[lastNegIndex+1:]))
    #     midProduct = 1 if firstNegIndex == lastNegIndex else self._product(nums[firstNegIndex+1:lastNegIndex])
    #     return midProduct* max(self._product(nums[:firstNegIndex+1]), self._product(nums[lastNegIndex:]))
    
    # def _product(self, nums: List[int]) -> int:
    #     product = 1
    #     for num in nums:
    #         product*num
    #     print('p', product, nums)
    #     return product

        

