class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if m == 1 or n == 1:
        #     return 1
        
        if m<n:
            m,n = n, m
        
        res = 1
        for j in range(1,n):
            res*= m+j-1
            res //= j
        return res

        
# (m + n - 2) c (n - 1)

# (m + n - 2)!
# (n-1)!(m-1)!

# (m*..m+n-2)
# n-1!
