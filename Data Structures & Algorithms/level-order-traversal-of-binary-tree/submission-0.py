# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # instantion of variables 
        output = []
        q = deque()
        q.append(root)
        while q:
            # read in current level / nodes
            currLevel = len(q)
            level = []

            # loop though process current level / prep next level
            for node in range(currLevel):
                node = q.popleft()
                if node:
                # add children for each node (creating new level)
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
            if level:
                output.append(level)
            # add processed current level to output
        return output
            


            



