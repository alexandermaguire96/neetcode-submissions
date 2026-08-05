# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = collections.deque()
        q.append(root)
        output = []
        if not root:
            return []
        while q:
            
            currLevel = len(q)
            for i in range(currLevel): 
                catch = q.popleft()
                if catch.left:
                    q.append(catch.left)
                if catch.right:
                    q.append(catch.right)
                if i == (currLevel -1) :
                    output.append(catch.val)

        return output
                
        
        # def dfs(root, output, depth):
        #     if not root:
        #         return output
        #     dfs(root.right, output, depth+1)
        #     dfs(root.left, output, depth+1)
        # dfs(root, output, 0)
        # return sorted(output)
            
            