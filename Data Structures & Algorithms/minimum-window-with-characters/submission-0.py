class Solution:
    def greaterThanEqual(self, currMap: {}, targetMap: {}) -> bool:
        for item in targetMap:
            if item not in currMap or currMap[item] < targetMap[item]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        targetMap, currMap = {}, {}

        for c in t:
            targetMap[c] = targetMap.get(c, 0) + 1
        
        res = ""

        i = 0

        for j in range(len(s)):
            if i==j and s[i] not in targetMap:
                i+=1
                continue
            c = s[j]
            if c in targetMap:
                currMap[c] = currMap.get(c, 0) + 1
                if currMap[c] == targetMap[c]:
                    if self.greaterThanEqual(currMap, targetMap):
                        if res == "" or len(res)>(j-i):
                            res = ""
                            for k in range(i,j+1):
                                print (1,i,j,k)
                                res += s[k]
                        currMap[s[i]] -= 1
                        i += 1
                        while i<j:
                            if not s[i] in targetMap:
                                i += 1
                            elif currMap[s[i]] > targetMap[s[i]]:
                                currMap[s[i]] -= 1
                                i += 1
                            else:
                                break
                elif currMap[c] > targetMap[c] and s[i] == c:
                    currMap[s[i]] -= 1
                    i += 1
                    while i<j:
                        if not s[i] in targetMap:
                            i += 1
                        elif currMap[s[i]] > targetMap[s[i]]:
                            currMap[s[i]] -= 1
                            i += 1
                        else:
                            break
            
        return res
                    
                



            
