class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {node: [] for node in range(n)}
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        visitingSet = set()
        def isNodeClean(node):
            print(node, adjList)
            if node in visitingSet:
                return False
            
            if len(adjList[node]) == 0:
                return True
            
            visitingSet.add(node)
            for child in adjList[node]:
                if node in adjList[child]:
                    adjList[child].remove(node)
                if not isNodeClean(child):
                    return False
            visitingSet.remove(node)
            adjList[node] = []
            return True
        
        if not isNodeClean(0):
            return False

        for node in range(1,n):
            if len(adjList[node]) >0: return False
        return True

        