class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])
        queue = []

        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        def treasure(i, j):

            for dx, dy in directions: 
                        
                next_i = i + dx
                next_j = j + dy

                if 0 <= next_i < rows and 0 <= next_j < cols:
                    if grid[i][j] + 1 < grid[next_i][next_j]:
                        grid[next_i][next_j] = grid[i][j] + 1
                        queue.append((next_i, next_j))

            return

        for i in range(rows):
                for j in range(cols):

                    if grid[i][j] == 0:

                        queue.append((i, j))
        
        i = 0
        while i < len(queue):

            row, col = queue[i]
            i += 1
            treasure(row, col)
        





            