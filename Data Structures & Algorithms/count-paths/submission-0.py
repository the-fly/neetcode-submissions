class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if(m<n):
        #     m,n = n,m
        # res = 0
        # currOptions = 1
        # for r in range(1,n+1):
        #     currOptions *= (m-r) // r
        #     res+= currOptions
        # return res

        pathToGetTo = [[1 for _ in range(n)] for _ in range(m)]
        print(pathToGetTo)
        pathToGetTo[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                up = pathToGetTo[i-1][j] if i>0 else 0
                left = pathToGetTo[i][j-1] if j>0 else 0
                pathToGetTo[i][j] = up + left
        return pathToGetTo[m-1][n-1]
        