class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        columns = len(grid[0])
        visited = set()

        islands = 0

        def visit(i,j):
            q = deque()
            visited.add((i,j))
            q.append((i,j))

            while q:
                i,j = q.popleft()
                directions = [(1,0), (0,1), (-1,0), (0,-1)]
                for di, dj in directions:
                    r = i+di
                    c = j+dj
                    if r in range(rows) and c in range(columns) and grid[i][j] == '1' and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c))
            return

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1' and (i,j) not in visited:
                    islands +=1
                    visit(i,j)
        return islands
        