# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minBound, maxBound = -1002, 1003
        def DFS(root, minBound, maxBound):
            if not root:
                return True

            if root.val <= minBound:
                return False
            elif root.val >= maxBound:
                return False
            

            return DFS(root.left, minBound, min(root.val, maxBound)) and DFS(root.right, max(minBound, root.val), maxBound)



        return DFS(root, minBound, maxBound)
