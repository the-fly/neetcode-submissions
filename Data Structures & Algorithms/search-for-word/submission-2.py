class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        columns = len(board[0])
        resSet = {()}

        def backtrack(x, y, index):
            if index == len(word):
                return True
            if  x>=rows or x<0 or y>=columns or y<0 or (x,y) in resSet or board[x][y] != word[index]:
                return False
            resSet.add((x,y))
            if backtrack(x+1, y, index + 1):
                return True
            if backtrack(x, y+1, index + 1):
                return True            
            if backtrack(x-1, y, index + 1):
                return True
            if backtrack(x, y-1, index + 1):
                return True
            resSet.remove((x,y))
            return False
            
        for i in range(rows):
            for j in range(columns):
                if backtrack(i, j, 0):
                    return True
        return False


        