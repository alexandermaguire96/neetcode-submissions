# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Tuple

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #Tuples can be imported if asked for, but not necessary in Python3
        def dfs(node) -> Tuple[bool, int]:

            if not node:
                return (True, 0)
            #determine if left is balanced, and height. 
            left_balance, left_height = dfs(node.left)
            #quick out in order to be more efficient. 
            if not left_balance:
                return (False,0)
            #repeat for right, now that left has been verified
            right_balance, right_height = dfs(node.right)
            if not right_balance:
                return (False,0)
            #abs because negative means nothing, it's the range we care abt. 
            balanced = abs(left_height - right_height) <= 1

            #return for the recursion
            return (balanced, max(left_height, right_height) + 1)

        #we don't need both values at end, just balanced or not
        balanced, _ = dfs(root)
        return balanced



        