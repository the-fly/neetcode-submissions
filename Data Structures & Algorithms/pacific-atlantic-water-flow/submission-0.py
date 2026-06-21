class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])
        res = []

        paAtReach = {(i, j): (False, False) for i in range(rows) for j in range(cols)}

        def bfs(i,j):
            q= deque()
            q.append((i,j))
            directions = [(+1,0), (-1,0), (0,1), (0,-1)]

            while(q):
                (i,j) = q.popleft()
                (pa, at) = paAtReach[(i,j)]
                for (di, dj) in directions:
                    r, c = i+di, j+dj
                    if r in range(rows) and c in range(cols) and heights[r][c] >= heights[i][j]:
                        if (pa and not paAtReach[(r,c)][0]) or (at and not paAtReach[(r,c)][1]):
                            paAtReach[(r,c)] = (pa or paAtReach[(r,c)][0], at or paAtReach[(r,c)][1])
                            q.append((r,c))

        for i in range(rows):
            paAtReach[(i,0)] = (True, paAtReach[(i,0)][1])
            # if i==0 or (i>0 and heights[i][0] < heights[i-1][0]):
            bfs(i,0)

            paAtReach[(i,cols-1)] = (paAtReach[(i,cols-1)][0], True)
            # if i== 0 or (i>0 and heights[i][cols-1] < heights[i-1][cols-1]):
            bfs(i,cols-1)

        for j in range(cols):
            paAtReach[(0,j)] = (True, paAtReach[(0,j)][1])

            # if j==0 or (j>0 and heights[0][j] < heights[0][j-1]):
            bfs(0,j)

            paAtReach[(rows-1,j)] = (paAtReach[(rows-1,j)][0], True)
            # if j==0 or (j>0 and heights[rows-1][j] < heights[rows-1][j]):
            bfs(rows-1,j)
        # print(paAtReach)

        for i in range(rows):
            for j in range(cols):
                if paAtReach[(i,j)] == (True, True):
                    res. append([i,j])
        return res