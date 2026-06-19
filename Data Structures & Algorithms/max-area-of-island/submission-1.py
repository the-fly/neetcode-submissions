class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        res = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        # curr = 0

        def visit(i,j):
            nonlocal curr
            q = deque()
            q.append((i,j))
            
            while(q):
                r,c = q.popleft()
                if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visited:
                    continue
                curr+=1
                visited.add((r,c))
                directions = [(+1,0),(0,+1),(-1,0),(0,-1)]
                for dr,dc in directions:
                    q.append((r+dr, c+dc))

        for i in range(rows):
            for j in range(cols):
                curr = 0
                visit(i,j)
                res = max(res,curr)
        return res
