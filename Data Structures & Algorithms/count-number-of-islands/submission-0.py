class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1, 0)]

        seen = set()
        count = 0

        def dfs(row, col, seen):

            if 0 > row or row >= rows or 0 > col or col >= cols:
                print("Passed boundary", row, col)
                return

            if (row, col) in seen:
                return

            if grid[row][col] == '0':
                return

            seen.add((row, col))    
            print("seen", seen)        

            for dr in directions:
                new_row = row + dr[0]
                new_col = col + dr[1]
                print("new" , new_row, new_col)
                
                dfs(new_row, new_col, seen)

                
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == "1":
                    if (row, col) not in seen:
                    
                        count += 1
                        print("original row", row, col)
                        dfs(row, col, seen)
 

        return count