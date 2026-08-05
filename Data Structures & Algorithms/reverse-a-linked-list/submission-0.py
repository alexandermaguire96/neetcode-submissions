# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        helper = ListNode()
        newHead = helper
        if head == None:
            return None

        def dfs(node):
            nonlocal helper
            
            if not node:
                return

            dfs(node.next)
            print(node.val, "current node")
            helper.next = ListNode(node.val)
            print(helper.val, "current helper node")
            
            helper = helper.next
            print(helper.val, "move?")
            
        dfs(head)
        return newHead.next