class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        #don't use embedded for loop, instead use bounds
        while top <= bottom and left <= right:

            #top row first, right+1 because non-inclusive
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            #down a row
            top += 1

            #right col
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            #left a col
            right -= 1

            #make sure in bounds before going back
            if top <= bottom:
                #bottom row
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                #up a row
                bottom -= 1
            
            #make sure in bound before going up
            if left <= right:
                #left col
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                #right a col
                left += 1

        return res
