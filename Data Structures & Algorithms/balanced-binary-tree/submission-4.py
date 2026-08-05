# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        def howdeep(node, count):

            if not node:
                return count

            deeperl = howdeep(node.left, count)
            deeperr = howdeep(node.right,count)
            deeper = max(deeperl, deeperr)
            return count + deeper

        left = howdeep(root.left, 1)
        right = howdeep(root.right, 1)
        print(left)
        print(right)
        difference = left - right
        print(difference)

        if abs(difference) >= 2:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


