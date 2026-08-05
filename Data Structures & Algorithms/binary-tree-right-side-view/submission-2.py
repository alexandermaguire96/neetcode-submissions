# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        output = []

        def dfs(root, output, depth):

            if not root:
                return None

            if len(output) == (depth):
                output.append(root.val)

            dfs(root.right, output, depth+1)
            dfs(root.left, output, depth+1)

        dfs(root, output, 0)
        return output
            
            