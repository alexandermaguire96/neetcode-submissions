"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

            if not node:
                return None

            newList = {}

            def dfs(original_node):
                
                if original_node in newList:
                    return newList[original_node]

                new_node = Node(original_node.val)
                newList[original_node] = new_node

                for neighbor in original_node.neighbors:
                    new_node.neighbors.append(dfs(neighbor))

                return new_node

            return dfs(node)

            print(newList)
