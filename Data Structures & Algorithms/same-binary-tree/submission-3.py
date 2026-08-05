# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #if there isn't a p or a q, then the trees are both empty and thus, the same
        if not p and not q:
            return True
        #if missing just one tree, not the same, or if the values aren't the same, not the same
        if not p or not q or p.val != q.val:
            return False
        #both sides need to pass, if both do then True, if either False, then False
        return (self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right))
        