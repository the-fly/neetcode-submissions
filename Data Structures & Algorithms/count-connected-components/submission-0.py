class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}

        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        res = 0
        for node in range(n):
            if len(adjList[node]) == 0:
                res += 1

        visitingSet = set()
        def dfs(node):
            if adjList[node] == []:
                return
            
            if node in visitingSet:
                return
            visitingSet.add(node)

            for child in adjList[node]:
                if adjList[child] != []:
                    if node in adjList[child]:
                        adjList[child].remove(node)
                        dfs(child)
            visitingSet.remove(node)
            adjList[node] = []
            return
        
        for node in range(n):
            if adjList[node] != []:
                dfs(node)
                res+=1
        return res



        