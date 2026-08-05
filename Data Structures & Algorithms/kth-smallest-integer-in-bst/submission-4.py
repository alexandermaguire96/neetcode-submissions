# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #need counter to be nonlocal
        counter = 0
        answer = None

        def dfs(root): 
            nonlocal counter
            nonlocal answer
            
            if not root:
                return
            
            if answer != None:
                return

            dfs(root.left)
            counter += 1
            print(root.val, counter)

            if counter == k:
                answer = root.val
                print('answer found', answer)
                return

            dfs(root.right)

            
                
        dfs(root)
        return answer
        




