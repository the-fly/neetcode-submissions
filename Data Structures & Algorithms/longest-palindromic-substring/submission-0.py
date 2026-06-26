class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        
        # OddLen Case
        span = 0
        resSet = [i for i in range(length)]
        currResOrigin = 0
        while resSet:
            span += 1
            newSet = []
            for origin in resSet:
                if (origin - span) in range(length) and (origin + span) in range(length) and s[origin-span] == s[origin + span]:
                    # print ('x', origin, span, s[origin-span], s[origin + span])
                    newSet.append(origin)
            resSet = newSet
            if resSet:
                currResOrigin = resSet[0]
            else:
                span -=1
        res1 = s[currResOrigin-span:currResOrigin+span+1]
            
        # EveenCase
        span = 0
        resSet = [i for i in range(length)]
        currResOrigin = 0
        while resSet:
            span += 1
            newSet = []
            for origin in resSet:
                if (origin - span) in range(length) and (origin + span -1) in range(length) and s[origin-span] == s[origin + span-1]:
                    # print ('y', origin, span, s[origin-span], s[origin + span])
                    newSet.append(origin)
            resSet = newSet
            if resSet:
                currResOrigin = resSet[0]
            else:
                span -=1
        res2 = s[currResOrigin-span:currResOrigin+span]

        if len(res2) > len(res1):
            return res2
        return res1




            


        