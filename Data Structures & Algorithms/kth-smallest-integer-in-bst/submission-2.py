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

        def dfs(root, k, answer): 
            nonlocal counter
            
            if not root:
                return -1

            answerLeft = dfs(root.left, k, answer)
            counter += 1
            print(root.val, counter)

            if counter == k:
                answer = root.val
                print('answer found', answer)
                return answer

            answerRight = dfs(root.right, k, answer)

            if counter == k and answerLeft == -1 and answerRight == -1:
                answer = root.val
                print('answer found', answer)
                return answer
            
            if answerLeft < 0 :
                return answerRight
            else:
                return answerLeft

        return dfs(root, k, -1)
        




