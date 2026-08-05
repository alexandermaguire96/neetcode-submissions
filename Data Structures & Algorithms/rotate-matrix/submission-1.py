class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # oldLeft = [row[0] for row in matrix]
        # oldRight = [row[-1] for row in matrix]
        # oldTop = matrix[0]
        # oldBottom = matrix[-1]

        # newLeft = []
        # newRight = []

        # for i in range(len(oldLeft)-1, -1, -1):
        #     newLeft.append(oldRight[i])

        # for i in range(len(oldRight)-1, -1, -1):
        #     newRight.append(oldLeft[i])

        # print(newRight)
        # print(newLeft)
        

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # for row in matrix:
        #     i, j = 0, len(row)-1
        #     while i < j:
        #         row[i], row[j] = row[j], row[i]
        #         i += 1
        #         j -= 1

        # for row in matrix:
        #     row.reverse()
            
        for row in matrix:
            row[:] = row[::-1]
        

