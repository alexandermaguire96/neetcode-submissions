# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):

            if not node:
                return (True, 0)

            left_balance, left_height = dfs(node.left)
            if not left_balance:
                return (False,0)
            right_balance, right_height = dfs(node.right)
            if not right_balance:
                return (False,0)

            balanced = abs(left_height - right_height) <= 1

            return (balanced, max(left_height, right_height) + 1)

        balanced, _ = dfs(root)
        return balanced



        