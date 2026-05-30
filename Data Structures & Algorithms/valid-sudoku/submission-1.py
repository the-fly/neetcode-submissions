class Solution:
    def valid(self, nums: List[str]) -> bool:
        count = {}
        for s in nums:
            if s != ".":
                count[s] = count.get(s,0) + 1 
                if count[s] > 1:
                    return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = True
        for i in range(9):
            row = board[i]
            col = [board[row][i] for row in range(9)]
            
            boxi, boxj = (i // 3)*3, (i%3)*3

            box =  [board[boxi][boxj], board[boxi][boxj+1], board[boxi][boxj+2], 
                    board[boxi+1][boxj], board[boxi+1][boxj+1], board[boxi+1][boxj+2], 
                    board[boxi+2][boxj], board[boxi+2][boxj+1], board[boxi+2][boxj+2]]

            if self.valid(col) and self.valid(row) and self.valid(box):
                continue
            else:
                return False
        return True
    