class Solution:

    
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])
        directions = [1,0,-1,0,1]

        def dfs(row, col):

            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != "O":
                return

            board[row][col] = "#"


            for i in range(len(directions)-1):

                dfs(row + directions[i], col + directions[i+1])
        

        for row in range(rows):
            for col in range(cols):

                if board[0][col] == "O":
                    dfs(0, col)

                elif board[-1][col] == "O":
                    dfs(rows-1, col)

                elif board[row][0] == "O":
                    dfs(row, 0)

                elif board[row][-1] == "O":
                    dfs(row, cols-1)

        for row in range(rows):
            for col in range(cols):

                if board[row][col] == "O":

                    board[row][col] = "X"

                elif board[row][col] == "#":

                    board[row][col] = "O"

                   