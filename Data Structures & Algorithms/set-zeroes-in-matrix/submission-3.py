class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row = len(matrix)
        col = len(matrix[0])
        firstRow = False


        for c in range(col):
            if matrix[0][c] == 0:
                firstRow = True

        for r in range(1, row):
            for c in range(col):

                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1,row):
            if matrix[r][0] == 0:
                for c in range(col):
                    matrix[r][c] = 0

        
        for c in range(1,col):
            if matrix[0][c] == 0:
                for r in range(row):
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0
        
        if firstRow == True:
            for c in range(col):
                matrix[0][c] = 0


                 


