# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Base Case
        #empty subRoot is a subRoot
        if not subRoot: return True
        #empty root, is impossible unless subroot also empty, 
        #which it isn't, because we checked. 
        if not root: return False

        #Are the whole trees just straight up the same?
        if self.sameTree(root, subRoot):
            return True

        #Ok, let's check down the line. 
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

        
    def sameTree(self, root, subRoot):
        #if there isn't a node in either tree, an empty is a sub of an empty
        if not root and not subRoot:
            return True
        #If there is a root node, and a subRoot node, and they're the same. 
        if root and subRoot and root.val == subRoot.val:
            #return - the tree is the same on left and right, True, or else False
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))
        #If the initial node on either tree is different:
        return False

        