class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows, cols = len(board) , len(board[0])
        seen_board = [[False for x in range(len(board[0]))] for _ in range(len(board))]
        
        def backtracking(i, j, path, index):
            # print(path + board[i][j], i, j)
            if word == path:
                print('word found')
                return True
            if i > rows -1 or j > cols - 1 or i < 0 or j < 0:
                print('super failed', i, j)
                return False

            if board[i][j] != word[index]:
                print('failed', i,j)
                return False
            print('dd')
            if seen_board[i][j] == True:
                return False
            seen_board[i][j] = True
            
            retval = (backtracking(i+1, j, path + board[i][j], index + 1) or
                    backtracking(i-1, j, path + board[i][j], index + 1) or
                    backtracking(i, j+1, path + board[i][j], index + 1) or
                    backtracking(i, j-1, path + board[i][j], index + 1) )
            seen_board[i][j] = False
            return retval
        ret_val = False
        for i in range(rows):
                for j in range(cols):
                    if board[i][j] == word[0]:
                        ret_val = backtracking(i, j, "", 0) or ret_val
        return ret_val


        