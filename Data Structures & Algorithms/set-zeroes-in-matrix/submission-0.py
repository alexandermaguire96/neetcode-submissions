class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row = len(matrix)
        col = len(matrix[0])

        zero_row = set()
        zero_col = set()

        for r in range(row):
            for c in range(col):

                if matrix[r][c] == 0:
                    zero_row.add(r)
                    zero_col.add(c)
                    print(zero_row, zero_col)

        for r in range(row):
            for c in range(col):

                if r in zero_row or c in zero_col:
                    matrix[r][c] = 0


                 


