# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        i = 0
        # root = TreeNode(preorder[0])

        def split(root, thestuff):
            left = thestuff[0:thestuff.index(root.val)]
            right = thestuff[thestuff.index(root.val)+1: len(thestuff)]
            return left, right


        def dfs(node, stuff, order):
            nonlocal i

            # if not node:
            #     return None
            if not order:
                return None

            root_val = preorder[i]
            node = TreeNode(root_val)
            i+=1

            left, right = split(node, order)

            node.left = dfs(node,stuff, left)
            node.right = dfs(node, stuff, right)
            return node



            
        
        node = dfs(None, preorder, inorder)

        return node