class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visitedSet = set()
        slength = len(s)
        visitingQ = []
        visitingQ.append(0)
        while visitingQ:
            originIndex = visitingQ.pop()
            visitedSet.add(originIndex)
            for word in wordDict:
                wordLen = len(word)
                if originIndex + wordLen <= slength and s[originIndex:originIndex + wordLen] == word:
                    nextOrigin = originIndex + wordLen
                    if nextOrigin == slength:
                        return True
                    if nextOrigin not in visitedSet and nextOrigin not in visitingQ:
                        visitingQ.append(nextOrigin)
        return False
                    

        
                