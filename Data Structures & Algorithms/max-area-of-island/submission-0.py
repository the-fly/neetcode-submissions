class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        res = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        # curr = 0

        def visit(i,j):
            nonlocal curr
            if i not in range(rows) or j not in range(cols) or grid[i][j] == 0 or (i,j) in visited:
                return
            curr+=1
            visited.add((i,j))

            directions = [(+1,0),(0,+1),(-1,0),(0,-1)]
            for dr,dc in directions:
                visit(i+dr, j+dc)

        for i in range(rows):
            for j in range(cols):
                curr = 0
                visit(i,j)
                res = max(res,curr)
        return res
