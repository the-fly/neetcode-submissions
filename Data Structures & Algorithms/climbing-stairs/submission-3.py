class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        
        curr = 1
        prev = 1
        index = 1

        while (index != n):
            prev, curr = curr, prev + curr
            index += 1
        return curr


        