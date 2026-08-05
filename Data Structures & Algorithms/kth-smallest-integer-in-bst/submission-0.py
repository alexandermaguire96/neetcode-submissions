# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        seen = []

        def dfs(root, k): 

            if not root:
                return

            seen.append(root.val)

            dfs(root.left, k)
            dfs(root.right, k)

        dfs(root, k)
        seen.sort()
        return seen[k-1]
        




