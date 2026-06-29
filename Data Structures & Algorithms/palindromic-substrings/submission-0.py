class Solution:
    def countSubstrings(self, s: str) -> int:
        
        length = len(s)
        res = 0
        
        # oddLen 
        oddOriginSet = set([a for a in range(length)])   
        evenOriginSet = set([a for a in range(length)])     
        span = 0
        while oddOriginSet or evenOriginSet:
            newOddSet = set()
            for origin in oddOriginSet:
                if origin-span in range(length) and origin+span in range(length) and s[origin-span] == s[origin+span]:
                    newOddSet.add(origin)
            oddOriginSet = newOddSet
            res+= len(oddOriginSet)

            newEvenSet = set()
            for origin in evenOriginSet:
                if origin-span in range(length) and origin+span+1 in range(length) and s[origin-span] == s[origin+span+1]:
                    newEvenSet.add(origin)
            evenOriginSet = newEvenSet
            res+= len(evenOriginSet)
            
            span += 1
        
        return res




