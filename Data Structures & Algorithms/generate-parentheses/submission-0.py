class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openCount = 0
        res = []
        currStr = ""

        def dfs(i):
            nonlocal openCount
            nonlocal currStr
            if i == 2*n and openCount == 0: 
                res.append(currStr) 
                print('a', i ,currStr)
                return
            # Extra closing bracket, not viable
            if openCount <0:
                return
            # More open brackets than possible, not viable
            if openCount - (2*n - i) > 0:
                return
            
            currStr += '('
            openCount += 1
            dfs(i+1)

            currStr = currStr[:-1]
            currStr += ')'
            openCount -= 2
            dfs(i+1)
            currStr = currStr[:-1]
            openCount += 1

            
        dfs(0)
        return res
