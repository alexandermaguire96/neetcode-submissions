class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(adjacency, visited, curNode):
            # base case
            if curNode in visited:
                return
            
            visited.add(curNode)
            # recursive step
            connectedNodes = adjacency[curNode]
            for nextNode in connectedNodes:
                dfs(adjacency, visited, nextNode)

            # return
            return 

        #instantiation
        adjacency = defaultdict(list)
        visited = set()
        graph = 0

        # adjaceny  matrix
        for edge in edges:
            adjacency[edge[0]].append(edge[1])
            adjacency[edge[1]].append(edge[0])


        # iteratioin
        # start point will always be 0 for dfs 
        numNodes = len(adjacency)
        # print(numNodes,adjacency)
        for i in range(numNodes):
            if i not in visited:
                dfs(adjacency, visited, i)
                graph += 1
        if len(visited) < n:
            graph += (n - len(visited))
        return graph