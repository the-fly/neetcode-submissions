class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        totalDays = len(temperatures)
        if totalDays == 0:
            return res

        reverseTempStack = [(temperatures[totalDays-1], totalDays-1)]
        res.append(0)
        
        for day in reversed(range(totalDays -1)):
            while (not len(reverseTempStack) == 0 and temperatures[day] >= reverseTempStack[-1][0]):
                reverseTempStack.pop()
            reverseTempStack.append((temperatures[day], day))

            if len(reverseTempStack) == 1:
                res.append(0)
            else: 
                res.append(reverseTempStack[-2][1] - day)            
        res1 = res[::-1]
        return res1
            


        