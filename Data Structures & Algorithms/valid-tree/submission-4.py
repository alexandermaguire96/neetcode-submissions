class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        seen = set()
        adjacent = defaultdict(list)

        #check if edge number is correct
        if len(edges) != (n-1):
            return False
        
        #adjacency matrix
        for edge in edges:
            adjacent[edge[0]].append(edge[1])
            adjacent[edge[1]].append(edge[0])

        # check adjacency matrix
        print(adjacent)

        def dfs(seen, adjacent, node):

            #base case
            if node in seen:
                return False

            seen.add(node)

            if len(seen) == n:
                print('finished')
                return True

            for value in adjacent[node]:
                
                c = dfs(seen, adjacent, value)
                if c == True:
                    break
            return c

        c = dfs(seen, adjacent, 0)
        return c