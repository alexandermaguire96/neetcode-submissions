class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def makePrefTree(trie):
            for word in words:
                root = trie
                for c in word:
                    if c not in root:
                        root[c] = {}
                    root = root[c]
                root["\0"] = True

        trie = {}
        makePrefTree(trie)

        # print(trie)

        rows = len(board)
        cols = len(board[0])
        res, visited = set(), [[False for _ in range(cols)] for _ in range(rows)]
        direction = [0, 1, 0, -1, 0]

        def dfs(row, col, trie, path):
            
            if visited[row][col] == True:
                return

            if "\0" in trie:
                res.add(path)
            

            visited[row][col] = True

            for i in range(4):
                newRow, newCol = row + direction[i], col + direction[i+1]
                if newRow >= 0 and newCol >= 0 and newRow < rows and newCol < cols:
                    if board[newRow][newCol] in trie:
                        dfs(newRow, newCol, trie[board[newRow][newCol]], path + board[newRow][newCol])
            
            visited[row][col] = False
            return
            

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie:
                    dfs(row, col, trie[board[row][col]], board[row][col])

        return list(res)