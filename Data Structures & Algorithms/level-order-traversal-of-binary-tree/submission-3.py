# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        def dfs(root, output, depth):

            if not root:
                return output

            if len(output) == depth:
                output.append([])
                
            dfs(root.left, output, depth+1)
            dfs(root.right, output, depth+1)
            
            output[depth].append(root.val)

            return output
        return dfs(root, output, 0)

            