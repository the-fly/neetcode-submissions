class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preSet = {crs:[] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            preSet[crs].append(pre)

        currVisiting = set()
        def dfs(crs):
            if crs in currVisiting:
                return False
            if len(preSet[crs]) == 0:
                return True
            
            currVisiting.add(crs)
            
            for pre in preSet[crs]:
                if not dfs(pre):
                    return False
            currVisiting.remove(crs)
            preSet[crs] = ()
            return True
        
        for crs in preSet:
            if not dfs(crs):
                return False
        return True
