class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n

        grid = [[1 for _ in range(cols)] for _ in range(rows)]
        

        for row in range(1,rows):
            for col in range(1,cols):
                    grid[row][col] = grid[row-1][col] + grid[row][col-1]

        return grid[-1][-1]

