# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root, upperBound, count):
            if not root:
                return 0
  
            upperBound = max(upperBound, root.val)
            if root.val >= upperBound:
                count = 1
            else: count = 0

            count += dfs(root.right, upperBound, count) 
            count += dfs(root.left, upperBound, count)

            return count
        count = dfs(root, root.val, count)
    
        return count
            

        