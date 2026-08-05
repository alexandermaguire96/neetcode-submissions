class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])
        
        pacificTop = set((0,c) for c in range(cols))
        pacificLeft = set((r, 0) for r in range(rows))
        atlanticRight = set((r, cols-1)for r in range(rows))
        atlanticBot = set((rows-1, c) for c in range(cols))

        pacific = pacificTop|pacificLeft
        atlantic = atlanticRight|atlanticBot

        pacificVisited = set()
        atlanticVisited = set()

        directions = [(0,1), (0, -1), (1,0), (-1, 0)]

        # Define your DFS function that takes (r, c) and a visited set

        def dfs(r, c, visited):

            if (r, c) in visited:
                return

            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if 0 <= nr < rows and 0 <= nc < cols:
                    # Height check: only go uphill or flat
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visited)
        # Call DFS on every cell in the Pacific set to fill the pacific reachable cells
        for r, c in pacific:
            dfs(r, c, pacificVisited)
        # Call DFS on every cell in the Atlantic set to fill the atlantic reachable cells
        for r, c in atlantic:
            dfs(r, c, atlanticVisited)
        # Return the intersection of the two visited sets

        return list(pacificVisited & atlanticVisited)
            