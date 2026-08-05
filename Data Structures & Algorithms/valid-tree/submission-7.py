class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        def dfs(connected, visited, node, parent):
            #base case
            if node in visited:
                return False

            #recursive call
            visited.add(node)
            for nextNode in connected[node]:
                if nextNode == parent:
                    continue
                if not dfs(connected, visited, nextNode, node):
                    return False
            #return 
            return True


        connected = defaultdict(list)
        visited = set()

        for edge in edges:
            connected[edge[0]].append(edge[1])
            connected[edge[1]].append(edge[0])

        # print(connected)

        res = dfs(connected, visited, 0, None)
        return res and len(visited) == n
