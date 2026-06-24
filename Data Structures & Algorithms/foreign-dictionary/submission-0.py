    
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adjList = {c: set() for word in words for c in word}

        for index in range(len(words)-1):
            prev, curr = words[index], words[index+1]

            minLen = min(len(prev), len(curr))
            if len(prev) > len(curr) and prev[:minLen] == curr[:minLen]:
                return ""
            
            for j in range(minLen):
                if prev[j] != curr[j]:
                    adjList[prev[j]].add(curr[j])
                    break
            
        visit = {} # visited if False, in path if True
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True

            for child in adjList[c]:
                if dfs(child):
                    return ""
            
            res.append(c)
            visit[c] = False
            return False
        
        for c in adjList:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)



    
    

    

                


    