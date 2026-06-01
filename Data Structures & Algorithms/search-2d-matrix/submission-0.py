class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        
        n = len(matrix[0])

        if n == 0:
            return False
        
        totalItems = m*n

        return self.binarySearch2D(matrix, target, n, 0, totalItems - 1)


    
    def binarySearch2D(self, matrix: List[List[int]], target: int, columnSize:int, left: int, right: int) -> bool:
        print(left, right)
        mid = left + (right - left) // 2
        i = self.itemIndex(columnSize, mid)

        if matrix[i[0]][i[1]] == target:
            return True
        
        if right <= left:
            return False
        

        
        if matrix[i[0]][i[1]] > target:
            return self.binarySearch2D(matrix, target, columnSize, left, mid-1)
        else:
            return self.binarySearch2D(matrix, target, columnSize, mid+1, right)

    def itemIndex(self, n: int, itemIndex: int) -> (int, int):
        i = itemIndex // n
        j = itemIndex%n
        return (i,j)


